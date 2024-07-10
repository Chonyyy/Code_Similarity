from antlr4 import *
import json, os
from parser.parser import *
from Word2Vec.word2vec import FeatureVectorizer
from collections import deque

PROJECTS_FOLDER = f'{os.getcwd()}/Projects/hulk/'

DATA_FOLDER = f'{os.getcwd()}/data/features_all/'
                                                          
DATA_FOLDER_VECT = f'{os.getcwd()}/data/features_vect/'

os.makedirs(DATA_FOLDER, exist_ok=True)

for f in os.scandir(PROJECTS_FOLDER):
    if f.is_dir():
        print(PROJECTS_FOLDER + f.name)
        
        output_json_path = os.path.join(DATA_FOLDER, f"features_{f.name}.json")
        output_json_path_vect = f'data/features_vect/features_{f.name}.json'
        # Dividimos la ruta en sus componentes
        components = PROJECTS_FOLDER.split(os.sep)
        folder_name = components[-2]
        
        if os.path.exists(output_json_path):
            if not os.path.exists(output_json_path_vect):
                try:
                    fv = FeatureVectorizer(output_json_path)
                    fv.vectorize_features_and_save(output_json_path_vect)
                except:
                    print("ERRRROOOOOORRRRR WORD2VEC")
            continue
        
        features = process_project(PROJECTS_FOLDER + f.name)
        features['project_name'] = f.name
        features['label'] = "original"
        
        
        if folder_name == "moogle":
            features['project_type'] = "moogle"
        elif folder_name == "wallE":
            features['project_type'] = "wallE"
        elif folder_name == "domino":
            features['project_type'] = "domino"
        elif folder_name == "hulk":
            features['project_type'] = "hulk"
        
        # Guardar los features en un archivo JSON
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(features, json_file, ensure_ascii=False, indent=4)
        
        print("Archivo JSON guardado correctamente.")
        
        try:
            fv = FeatureVectorizer(output_json_path)
            fv.vectorize_features_and_save(output_json_path_vect)
        except:
            print("ERRRROOOOOORRRRR WORD2VEC")

# Lista para almacenar todos los datos de los archivos JSON
datos_combinados = []

# Iterar sobre cada archivo en el directorio
for filename in os.listdir(DATA_FOLDER_VECT):
    if filename.endswith('.json'):
        path = os.path.join(DATA_FOLDER_VECT, filename)
        
        # Leer el archivo JSON y cargar los datos
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Agregar los datos al lista
            datos_combinados.append(data)

# Escribir todos los datos combinados en un nuevo archivo JSON
merged_path = DATA_FOLDER = f'{os.getcwd()}/data/merged_features.json'
with open(merged_path, 'w', encoding='utf-8') as f:
    json.dump(datos_combinados, f, ensure_ascii=False, indent=4)

print(f'Se han combinado {len(datos_combinados)} archivos JSON en {merged_path}')


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
        # print(type(current_node).__name__)
        
        try:
            print(current_node.symbol.text)
        except:
            for child in current_node.children:
                    queue.append(child)
