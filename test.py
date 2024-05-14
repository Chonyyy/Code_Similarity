from antlr4 import *
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser

def parse_file(file_path):
    input_stream = FileStream(file_path)
    lexer = CSharpLexer(input_stream, None)
    stream = CommonTokenStream(lexer)
    parser = CSharpParser(stream)
    
    tree = parser.compilation_unit()  
    
    print(tree.toStringTree(recog=parser))
    pass

parse_file("CSharp/examples/archivo_csharp.cs")
