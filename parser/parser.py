import os
from antlr4 import InputStream, CommonTokenStream
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser
from collections import deque

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