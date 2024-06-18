from antlr4 import *
from antlr4.tree.Tree import ErrorNodeImpl
import json, os, time
from listener import FeatureExtractorListener, walk_tree
from antlr4 import InputStream, CommonTokenStream
from Python.CSharpLexer import CSharpLexer
from Python.CSharpParser import CSharpParser
from parser.parser import *


PROJECTS_FOLDER = f'{os.getcwd()}/Projects/'

DATA_FOLDER = f'{os.getcwd()}/data/'

os.makedirs(DATA_FOLDER, exist_ok=True)


for f in os.scandir(PROJECTS_FOLDER):
    if f.is_dir():
        print(PROJECTS_FOLDER + f.name)
        
        output_json_path = os.path.join(DATA_FOLDER, f"features_{f.name}.json")
        
        if os.path.exists(output_json_path):
            continue
        
        features = process_project(PROJECTS_FOLDER + f.name)
        features['project_name'] = f.name
        features['label'] = "original"

        # Guardar los features en un archivo JSON
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(features, json_file, ensure_ascii=False, indent=4)


