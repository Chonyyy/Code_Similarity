import json, os
import itertools
import numpy as np


def load_projects_from_json(json_file):
    with open(json_file, 'r') as f:
        projects = json.load(f)
    return projects

def generate_pairs(projects):
    pairs = []
    for (proj1, proj2) in itertools.combinations(projects, 2):
        pair = {
            "project_1": proj1,
            "project_2": proj2,
            "similarity_flag": 1 if proj1["label"] == f"copy_of_{proj2['project_name']}" or proj2["label"] == f"copy_of_{proj1['project_name']}" else 0
        }
        pairs.append(pair)
    return pairs

# Ruta al directorio que contiene los archivos JSON de los proyectos
projects_directory = "data/features_domino"

# Lista para almacenar todos los proyectos cargados
all_projects = []

# Cargar todos los proyectos desde los archivos JSON en el directorio
for filename in os.listdir(projects_directory):
    if filename.endswith(".json"):
        file_path = os.path.join(projects_directory, filename)
        projects = load_projects_from_json(file_path)
        all_projects.append(projects)

# Generar los pares de entrenamiento
pairs = generate_pairs(all_projects)

# Guardar los pares en un archivo JSON
with open('training_pairs.json', 'w') as f:
    json.dump(pairs, f, indent=4)
    

# # Convertir a arrays NumPy
# def dict_to_vector(d):
#     # Convertir las características a un solo vector
#     vector = []
#     for key in sorted(d.keys()):
#         value = d[key]
#         if isinstance(value, list):
#             vector.extend(value)
#         else:
#             vector.append(value)
#     return np.array(vector)

# data_a_vectors = np.array([dict_to_vector(pair['code_a']) for pair in data['pairs']])
# data_b_vectors = np.array([dict_to_vector(pair['code_b']) for pair in data['pairs']])
# labels = np.array([pair['label'] for pair in data['pairs']])

# print("data_a_vectors shape:", data_a_vectors.shape)
# print("data_b_vectors shape:", data_b_vectors.shape)
# print("labels shape:", labels.shape)