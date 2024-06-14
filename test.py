import json, time, os
from listener import FeatureExtractorListener, walk_tree
from parser.parser import parse_project, bfs_tree

PROJECTS_FOLDER = f'{os.getcwd()}/Projects/'

DATA_FOLDER = f'{os.getcwd()}/data/'

os.makedirs(DATA_FOLDER, exist_ok=True)

project_features = []

for f in os.scandir(PROJECTS_FOLDER):
    if f.is_dir():
        ast = parse_project(PROJECTS_FOLDER + f.name)
        
        extractor = FeatureExtractorListener()
        walk_tree(extractor, ast)
        features = extractor.get_features()
        features['project_name'] = f.name
        project_features.append(features)
        # Imprimir el arbol para debuggear
        # bfs_tree(ast)
        
# Generar un nombre de archivo JSON único usando la marca de tiempo
timestamp = time.strftime("%Y%m%d-%H%M%S")
output_json_path = os.path.join(DATA_FOLDER, f"features_{timestamp}.json")

# Guardar los features en un archivo JSON
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(project_features, json_file, ensure_ascii=False, indent=4)
