from antlr4 import Parser

class CSharpParserBase(Parser):
    def init(self, input, output=None, error_output=None):
        super().init(input, output, error_output)

    def is_local_variable_declaration(self):
        local_var_decl = self._ctx  # this is equivalent to 'this.Context' in C#
        if not isinstance(local_var_decl, CSharpParser.Local_variable_declarationContext):
            return True
        local_variable_type = local_var_decl.local_variable_type()
        if local_variable_type is None:
            return True
        if local_variable_type.getText() == "var":
            return False
        return True