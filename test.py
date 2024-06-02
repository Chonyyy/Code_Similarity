from antlr4 import *
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser
from collections import deque
from listener import FeatureExtractorListener, walk_tree

def parse_file(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = CSharpLexer(input_stream, None)
    stream = CommonTokenStream(lexer)
    parser = CSharpParser(stream)
    
    tree = parser.compilation_unit()     
    root_node = tree.children[0] 
    
    extractor = FeatureExtractorListener()
    walk_tree(extractor, tree)
    features = extractor.get_features()
    
    pass

    # print(tree.toStringTree(recog=parser))
    bfs_tree(tree)

    pass

from collections import deque

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
            if not current_node.children == None:
                for child in current_node.children:
                        queue.append(child)


parse_file("CSharp/examples/archivo_csharp.cs")
