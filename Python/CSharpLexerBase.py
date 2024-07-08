from antlr4 import Lexer, CommonTokenStream
from collections import deque

class CSharpLexerBase(Lexer):
    def init(self, input, output=None, error_output=None):
        super().init(input, output, error_output)
        self._input = input
        self.interpolatedStringLevel = 0
        self.interpolatedVerbatiums = deque()
        self.curlyLevels = deque()
        self.verbatium = False

    def on_interpolated_regular_string_start(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(False)
        self.verbatium = False

    def on_interpolated_verbatium_string_start(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(True)
        self.verbatium = True

    def on_open_brace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels.append(self.curlyLevels.pop() + 1)

    def on_close_brace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels.append(self.curlyLevels.pop() - 1)
            if self.curlyLevels[-1] == 0:
                self.curlyLevels.pop()
                self.skip()
                self.popMode()

    def on_colon(self):
        if self.interpolatedStringLevel > 0:
            ind = 1
            switch_to_format_string = True
            while chr(self._input.LA(ind)) != '}':
                if self._input.LA(ind) in [ord(':'), ord(')')]:
                    switch_to_format_string = False
                    break
                ind += 1
            if switch_to_format_string:
                self.mode(CSharpLexer.INTERPOLATION_FORMAT)

    def open_brace_inside(self):
        self.curlyLevels.append(1)

    def on_double_quote_inside(self):
        self.interpolatedStringLevel -= 1
        self.interpolatedVerbatiums.pop()
        self.verbatium = self.interpolatedVerbatiums[-1] if self.interpolatedVerbatiums else False

    def on_close_brace_inside(self):
        self.curlyLevels.pop()

    def is_regular_char_inside(self):
        return not self.verbatium

    def is_verbatium_double_quote_inside(self):
        return self.verbatium