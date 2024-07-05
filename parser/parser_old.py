import os
from antlr4 import InputStream, CommonTokenStream
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser
from antlr4.error.ErrorListener import ErrorListener
from collections import deque

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)
        print(error_message)

    def reportTokenRecognitionError(self, recognizer, e):
        token = e.offendingToken
        error_message = f"Token recognition error at line {token.line}:{token.column} token recognition error at: '{token.text}'"
        self.errors.append(error_message)
        print(error_message)

def parse_project(project_addr):
    combined_content = ""

    # Recorrer recursivamente el directorio y subdirectorios
    for root, _, files in os.walk(project_addr):
        for filename in files:
            if filename.endswith(".cs"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        combined_content += file.read() + "\n"
                except UnicodeDecodeError:
                    try:
                        with open(file_path, 'r', encoding='iso-8859-1') as file:
                            combined_content += file.read() + "\n"
                    except UnicodeDecodeError:
                        print("Codificación desconocida")
                    
    input_stream = InputStream(combined_content)
    lexer = CSharpLexer(input_stream, None)
    stream = CommonTokenStream(lexer)
    parser = CSharpParser(stream)    
    
    # Configura el custom error listener
    error_listener = CustomErrorListener()
    lexer.removeErrorListeners()  # Remueve los error listeners por defecto
    lexer.addErrorListener(error_listener)
    parser.removeErrorListeners()  # Remueve los error listeners por defecto
    parser.addErrorListener(error_listener)

    # Manejo de errores encontrados
    if error_listener.errors:
        print("Errors encountered during parsing:")
        for error in error_listener.errors:
            print(error)
            
    tree = parser.compilation_unit()
    
    return tree

def bfs_tree(tree):
    """
    Realiza una búsqueda en amplitud (BFS) sobre el árbol de análisis sintáctico.
    
    param tree: El árbol de análisis sintáctico generado por ANTLR.
    """
    
    queue = deque([tree])
    
    while queue:
        # Sacar el primer nodo de la cola
        current_node = queue.popleft()
        
        # Imprimir el tipo de nodo
        print(type(current_node).__name__)
        
        try:
            print(current_node.symbol.text)
        except:
            if current_node.children is not None:
                for child in current_node.children:
                    queue.append(child)