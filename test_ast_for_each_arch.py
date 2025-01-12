import os
import json
from antlr4 import *
from parser.parser import process_project
from embedding.word2vec import FeatureVectorizer

class ProjectFeatureProcessor:
    def __init__(self, projects_folder, data_folder, data_vect_folder):
        self.projects_folder = projects_folder
        self.data_folder = data_folder
        self.data_vect_folder = data_vect_folder
        os.makedirs(self.data_folder, exist_ok=True)
        os.makedirs(self.data_vect_folder, exist_ok=True)

    def process_projects(self):
        """Procesa todos los proyectos en la carpeta especificada."""
        for project in os.scandir(self.projects_folder):
            if project.is_dir():
                print(f"Procesando: {self.projects_folder + project.name}")
                self._process_single_project(project)

    def _process_single_project(self, project):
        """Procesa un único proyecto y guarda los resultados en JSON y vectores."""
        output_json_path = os.path.join(self.data_folder, f"features_{project.name}.json")
        output_json_path_vect = os.path.join(self.data_vect_folder, f"features_{project.name[:-3]}.json")

        if os.path.exists(output_json_path):
            if not os.path.exists(output_json_path_vect):
                fv = FeatureVectorizer(output_json_path)
                fv.vectorize_features_and_save(output_json_path_vect)
            return

        features = process_project(self.projects_folder + project.name)
        features['project_name'] = project.name
        features['label'] = self._determine_label(project.name)

        self._save_json(output_json_path, features)
        print("Archivo JSON guardado correctamente.")

        fv = FeatureVectorizer(output_json_path)
        fv.vectorize_features_and_save(output_json_path_vect)

    def _determine_label(self, project_name):
        """Determina la etiqueta del proyecto."""
        if "copy_of" in project_name:
            start_index = project_name.index("copy_of")
            return project_name[start_index:]
        return "original"

    def _save_json(self, path, data):
        """Guarda un diccionario como archivo JSON."""
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def combine_feature_vectors(self, output_file):
        """Combina todos los vectores de características en un único archivo JSON."""
        combined_data = []

        for filename in os.listdir(self.data_vect_folder):
            if filename.endswith('.json'):
                path = os.path.join(self.data_vect_folder, filename)
                with open(path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    combined_data.append(data)

        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(combined_data, file, ensure_ascii=False, indent=4)

        print(f"Se han combinado {len(combined_data)} archivos JSON en {output_file}")

if __name__ == "__main__":
    PROJECTS_FOLDER = f'{os.getcwd()}/Projects/pruebas/Moogle/'
    DATA_FOLDER = f'{os.getcwd()}/data/pruebas/Moogle/features'
    DATA_FOLDER_VECT = f'{os.getcwd()}/data/pruebas/Moogle/features_vect'

    processor = ProjectFeatureProcessor(PROJECTS_FOLDER, DATA_FOLDER, DATA_FOLDER_VECT)

    # Procesar proyectos
    processor.process_projects()

    # # Combinar vectores de características
    # MERGED_PATH = f'{os.getcwd()}/data/merged_features.json'
    # processor.combine_feature_vectors(MERGED_PATH)
