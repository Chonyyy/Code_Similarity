from antlr4 import *
from antlr4.tree.Tree import ErrorNodeImpl
import json, os, time
from listener import FeatureExtractorListener, walk_tree
from antlr4 import InputStream, CommonTokenStream
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser

def extract_features_from_file(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = CSharpLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CSharpParser(tokens)

    # Agrega tu listener de errores personalizado aquí si es necesario

    tree = parser.compilation_unit()
    extractor = FeatureExtractorListener()
    walk_tree(extractor, tree)
    return extractor.get_features()

def combine_features(all_features):
    combined_features = {}

    for features in all_features:
        for key, value in features.items():
            if isinstance(value, dict):
                if key not in combined_features:
                    combined_features[key] = {}
                for sub_key, sub_value in value.items():
                    if sub_key not in combined_features[key]: 
                        if isinstance(sub_value, int):
                            combined_features[key][sub_key] = 0
                        elif isinstance(sub_value, str):
                            combined_features[key][sub_key] = sub_value
                        elif isinstance(sub_value, dict):
                            combined_features[key][sub_key] = {}

                    if isinstance(sub_value, int):
                        combined_features[key][sub_key] += sub_value

                    elif isinstance(sub_value, dict):
                        # Combinar los sub-diccionarios recursivamente
                        for inner_key, inner_value in sub_value.items():
                            if inner_key not in combined_features[key][sub_key]:
                                if isinstance(inner_value, int):
                                    combined_features[key][sub_key][inner_key] = 0
                                elif isinstance(inner_value, str):
                                    combined_features[key][sub_key][inner_key] = inner_value
                            if isinstance(inner_value, int):
                                combined_features[key][sub_key][inner_key] += inner_value

            elif isinstance(value, list):
                if key not in combined_features:
                    combined_features[key] = []
                
                combined_features[key] += value
                    
            else:
                if key not in combined_features:
                    combined_features[key] = 0
                combined_features[key] += value

    return combined_features

def process_project(root_directory):
    all_features = []

    for subdir, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".cs"):
                file_path = os.path.join(subdir, file)
                try:
                    features = extract_features_from_file(file_path)
                    all_features.append(features)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    combined_features = combine_features(all_features)
    return combined_features
    

if __name__ == "__main__":
    
    PROJECTS_FOLDER = f'{os.getcwd()}/Projects/'

    DATA_FOLDER = f'{os.getcwd()}/data/'

    os.makedirs(DATA_FOLDER, exist_ok=True)

    project_features = []

    for f in os.scandir(PROJECTS_FOLDER):
        if f.is_dir():
            print(PROJECTS_FOLDER + f.name)
            
            features = process_project(PROJECTS_FOLDER + f.name)
            features['project_name'] = f.name
            project_features.append(features)
            
    # Generar un nombre de archivo JSON único usando la marca de tiempo
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_json_path = os.path.join(DATA_FOLDER, f"features_{timestamp}.json")

    # Guardar los features en un archivo JSON
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(project_features, json_file, ensure_ascii=False, indent=4)


