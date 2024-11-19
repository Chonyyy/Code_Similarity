import json, os
import itertools
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

class PrepareDataSNN:
    def __init__(self):
        self.projects_directory = f'{os.getcwd()}/data/features_vect_others/'
        self.all_projects = []

    def _load_projects_from_json(self, json_file):
        with open(json_file, 'r') as f:
            projects = json.load(f)
        return projects

    def ensure_length(self, vector, length):
        return (vector + [0] * length)[:length]

    def _extract_features(self, json_data):
        features = [
            json_data.get("total_nodes", 0),
            json_data.get("max_depth", 0),
            json_data.get("number_of_variables", 0),
            json_data.get("number_of_constants", 0),
            json_data.get("out_variables", 0),
            json_data.get("ref_params", 0),
            json_data.get("number_of_methods", 0),
            json_data.get("number_of_classes", 0),
            json_data.get("number_of_interfaces", 0),
            json_data.get("number_of_abstract_classes", 0),
            json_data.get("number_of_sealed_classes", 0),
            json_data.get("import_statements", 0),
            json_data.get("number_of_try_blocks", 0),
            json_data.get("number_of_lists", 0),
            json_data.get("number_of_dictionaries", 0),
            json_data.get("number_of_enums", 0),
            json_data.get("number_of_delegates", 0),
            json_data.get("function_calls", 0),
            json_data.get("control_structures_if", 0),
            json_data.get("control_structures_switch", 0),
            json_data.get("control_structures_for", 0),
            json_data.get("control_structures_while", 0),
            json_data.get("control_structures_dowhile", 0),
            json_data.get("access_modifiers_public", 0),
            json_data.get("access_modifiers_private", 0),
            json_data.get("access_modifiers_protected", 0),
            json_data.get("access_modifiers_internal", 0),
            json_data.get("access_modifiers_static", 0),
            json_data.get("access_modifiers_protected_internal", 0),
            json_data.get("access_modifiers_private_protected", 0),
            json_data.get("modifier_readonly", 0),
            json_data.get("modifier_volatile", 0),
            json_data.get("modifier_virtual", 0),
            json_data.get("modifier_override", 0),
            json_data.get("modifier_new", 0),
            json_data.get("modifier_partial", 0),
            json_data.get("modifier_extern", 0),
            json_data.get("modifier_unsafe", 0),
            json_data.get("modifier_async", 0),
            json_data.get("linq_querie_select", 0),
            json_data.get("linq_queries_where", 0),
            json_data.get("linq_queries_orderBy", 0),
            json_data.get("linq_queries_groupBy", 0),
            json_data.get("linq_queries_join", 0),
            json_data.get("linq_queries_sum", 0),
            json_data.get("linq_queries_count", 0),
            json_data.get("library_call_console", 0),
            json_data.get("library_call_math", 0),
            json_data.get("number_of_lambdas", 0),
            json_data.get("number_of_getters", 0),
            json_data.get("number_of_setters", 0),
            json_data.get("number_of_tuples", 0),
            json_data.get("number_of_namespaces", 0),
            *self.ensure_length(json_data.get("variable_names_vector", []), 2),
            *self.ensure_length(json_data.get("method_return_types_vector", []), 2),
            *self.ensure_length(json_data.get("method_names_vector", []), 2),
            *self.ensure_length(json_data.get("class_names_vector", []), 2),
            *self.ensure_length(json_data.get("method_parameters_vector", []), 4),
        ]


        l = len(features)
        if l == 63:
            pass
        return np.array(features)

    def _generate_pairs(self, projects):
        pairs = []
        for (proj1, proj2) in itertools.combinations(projects, 2):
            pair = {
                "project_1": self._extract_features(proj1),
                "project_2": self._extract_features(proj2),
                "similarity_flag": 1 if proj1["label"] == f"copy_of_{proj2['project_name']}" or proj2["label"] == f"copy_of_{proj1['project_name']}" else 0
            }
            pairs.append(pair)
        return pairs

    def _load_all_project(self):
        # Cargar todos los proyectos desde los archivos JSON en el directorio
        for filename in os.listdir(self.projects_directory):
            if filename.endswith(".json"):
                file_path = os.path.join(self.projects_directory, filename)
                projects = self._load_projects_from_json(file_path)
                self.all_projects.append(projects)

    def process(self): 
        self._load_all_project()
        self._generate_pairs(self.all_projects)
        # Generar los pares de entrenamiento
        pairs = self._generate_pairs(self.all_projects)

        labels = np.array([pair["similarity_flag"] for pair in pairs])
        data_a = np.array([pair["project_1"] for pair in pairs])
        data_b = np.array([pair["project_2"] for pair in pairs])

        # Normalizar los datos
        scaler = StandardScaler()
        data_a = scaler.fit_transform(data_a)
        data_b = scaler.transform(data_b)

        # Guardar los pares en un archivo JSON
        with open('training_pairs.json', 'wb') as f:
            pickle.dump(pairs, f)
        
        return data_a, data_b, labels


if __name__ == "__main__":
    data = PrepareDataSNN()
    res = data.process()
