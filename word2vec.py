import json
import numpy as np
from gensim.models import Word2Vec

# Cargar las características desde un archivo JSON
with open('data/features_domino/features_Domino-Project-master.json', 'r') as f:
    features = json.load(f)
    
# Extraer todas las listas de strings
variable_names = [item for sublist in features["variable_names"] for item in sublist]
method_names = features["method_names"]
class_names = features["class_names"]
interface_names = features["interface_names"]

# Unir todas las listas de strings en una lista única para entrenar el modelo Word2Vec
all_words = variable_names + method_names + class_names + interface_names
sentences = [all_words]  # Se entrena en una lista que contiene todas las palabras

# Entrenar el modelo Word2Vec
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=1)

# Función para convertir una lista de palabras a vectores
def vectorize_strings_list(strings_list, model):
    vectors = []
    for word in strings_list:
        if word in model.wv:
            vectors.append(model.wv[word])
        else:
            vectors.append(np.zeros(model.vector_size))
    return np.mean(vectors, axis=0)

# Convertir vectores de numpy a listas
def convert_ndarray_to_list(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            convert_ndarray_to_list(value)
        elif isinstance(value, np.ndarray):
            dictionary[key] = value.tolist()
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, np.ndarray):
                    value[i] = item.tolist()
                elif isinstance(item, list):
                    for j, subitem in enumerate(item):
                        if isinstance(subitem, np.ndarray):
                            item[j] = subitem.tolist()

# Convertir y reemplazar las listas de strings con sus representaciones vectoriales
features['variable_names_vector'] = [vectorize_strings_list(sublist, model) for sublist in features['variable_names']]
features['method_return_types_vector'] = [vectorize_strings_list(sublist, model) for sublist in features['method_return_types']]
features['method_names_vector'] = vectorize_strings_list(features['method_names'], model)
features['class_names_vector'] = vectorize_strings_list(features['class_names'], model)
features['interface_names_vector'] = vectorize_strings_list(features['interface_names'], model)

# Eliminar las listas de strings originales del diccionario
del features['variable_names']
del features['method_names']
del features['class_names']
del features['interface_names']

# Convertir ndarrays a listas para JSON serializable
convert_ndarray_to_list(features)

# Guardar el diccionario actualizado como un archivo JSON
with open('path_to_output_features.json', 'w') as f:
    json.dump(features, f, indent=4)

print("Archivo JSON guardado correctamente.")
