import os
import json, time
from antlr4 import *
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser
from collections import deque
from listener import FeatureExtractorListener, walk_tree

def parse_files_in_directory(directory_path,  output_directory):
    combined_content = ""

    # Recorrer recursivamente el directorio y subdirectorios
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".cs"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    combined_content += file.read() + "\n"

    input_stream = InputStream(combined_content)
    lexer = CSharpLexer(input_stream, None)
    stream = CommonTokenStream(lexer)
    parser = CSharpParser(stream)    
    tree = parser.compilation_unit()

    extractor = FeatureExtractorListener()
    walk_tree(extractor, tree)
    features = extractor.get_features()
    
    # Generar un nombre de archivo JSON único usando la marca de tiempo
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_json_path = os.path.join(output_directory, f"features_{timestamp}.json")
    
    # Guardar los features en un archivo JSON
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(features, json_file, ensure_ascii=False, indent=4)
    
    print(f"Features saved to {output_json_path}")
    
    # bfs_tree(tree)
    pass

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


# Directorio que contiene los archivos .cs
# directory_path = "CSharp/examples_ok/"
directory_path = "C:/Users/Chony/Downloads/moogle-main/moogle-main/"

# Directorio donde se guardarán los archivos JSON de salida
output_directory = "Features/"

# Crear el directorio de salida si no existe
os.makedirs(output_directory, exist_ok=True)

parse_files_in_directory(directory_path, output_directory)
