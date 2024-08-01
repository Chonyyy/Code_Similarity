from antlr4 import *
import os
from listener import FeatureExtractorListener, walk_tree
from antlr4 import CommonTokenStream
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
                        elif isinstance(sub_value, tuple):
                            combined_features[key][sub_key] = ()

                    if isinstance(sub_value, int):
                        combined_features[key][sub_key] += sub_value
                        
                    if isinstance(sub_value, tuple):
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

            elif isinstance(value, set):
                if key not in combined_features:
                    combined_features[key] = []
                
                combined_features[key] += list(value)
                    
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
    