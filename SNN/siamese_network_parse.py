import json, os
import itertools
import numpy as np
from sklearn.preprocessing import StandardScaler
import json, os
import itertools
import numpy as np
from sklearn.preprocessing import StandardScaler


class PrepareDataSNN:
    def __init__(self):
        self.projects_directory = f'{os.getcwd()}/data/features_vect/'
        self.all_projects = []

    def _load_projects_from_json(self, json_file):
        with open(json_file, 'r') as f:
            projects = json.load(f)
        return projects

    def _extract_features(self, json_data):
        features = [
            json_data["total_nodes"],
            json_data["max_depth"],
            json_data["number_of_variables"],
            json_data["number_of_constants"],
            json_data["out_variables"],
            json_data["ref_params"],
            json_data["number_of_methods"],
            json_data["number_of_classes"],
            json_data["number_of_interfaces"],
            json_data["number_of_abstract_classes"],
            json_data["number_of_sealed_classes"],
            json_data["import_statements"],
            json_data["number_of_try_blocks"],
            json_data["number_of_lists"],
            json_data["number_of_dictionaries"],
            json_data["number_of_enums"],
            json_data["number_of_delegates"],
            json_data["function_calls"],
            json_data["control_structures_if"],
            json_data["control_structures_switch"],
            json_data["control_structures_for"],
            json_data["control_structures_while"],
            json_data["control_structures_dowhile"],
            json_data["access_modifiers_public"],
            json_data["access_modifiers_private"],
            json_data["access_modifiers_protected"],
            json_data["access_modifiers_internal"],
            json_data["access_modifiers_static"],
            json_data["access_modifiers_protected_internal"],
            json_data["access_modifiers_private_protected"],
            json_data["modifier_readonly"],
            json_data["modifier_volatile"],
            json_data["modifier_virtual"],
            json_data["modifier_override"],
            json_data["modifier_new"],
            json_data["modifier_partial"],
            json_data["modifier_extern"],
            json_data["modifier_unsafe"],
            json_data["modifier_async"],
            json_data["linq_querie_select"],
            json_data["linq_queries_where"],
            json_data["linq_queries_orderBy"],
            json_data["linq_queries_groupBy"],
            json_data["linq_queries_join"],
            json_data["linq_queries_sum"],
            json_data["linq_queries_count"],
            json_data["library_call_console"],
            json_data["library_call_math"],
            json_data["number_of_lambdas"],
            json_data["number_of_getters"],
            json_data["number_of_setters"],
            json_data["number_of_tuples"],
            json_data["number_of_namespaces"],
            *json_data["variable_names_vector"],
            *json_data["method_return_types_vector"],
            *json_data["method_names_vector"],
            *json_data["class_names_vector"],
            *json_data["method_parameters_vector"]
        ]
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

        # Extraer las características de los pares
        data_a = np.array([pair["project_1"] for pair in pairs])
        data_b = np.array([pair["project_2"] for pair in pairs])
        labels = np.array([pair["similarity_flag"] for pair in pairs])

        # Normalizar los datos
        # scaler = StandardScaler()
        # data_a = scaler.fit_transform(data_a)
        # data_b = scaler.transform(data_b)

        # Guardar los pares en un archivo JSON
        # with open('training_pairs.json', 'w') as f:
        #     json.dump(pairs, f, indent=4)
        
        return data_a, data_b, labels


if __name__ == "__main__":
    data = PrepareDataSNN()
    res = data.process()
