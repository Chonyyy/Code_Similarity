import json
import numpy as np
from gensim.models import Word2Vec
import os

class FeatureVectorizer:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.features = None
        self.model = None
        
    def load_features_from_json(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as f:
            self.features = json.load(f)
    
    def extract_string_lists(self):
        variable_names = [item for sublist in self.features["variable_names"] for item in sublist]
        delegate_names = [item for sublist in self.features["delegate_names"] for item in sublist]
        method_return_types = [item for sublist in self.features["method_return_types"] for item in sublist]
        method_names = self.features["method_names"]
        class_names = self.features["class_names"]
        interface_names = self.features["interface_names"]
        enums_names = self.features["enums_names"]
        params_names = []
        
        for method in self.features['method_parameters']:
            params_names.append(method[0])
            for param in method[1]:
                params_names.append(param[0])
                params_names.append(param[1])
        
        all_words = (variable_names + method_names + class_names + interface_names +
                     enums_names + delegate_names + params_names + method_return_types)
        
        self.sentences = [all_words]
    
    def train_word2vec_model(self, vector_size=2, window=5, min_count=1, sg=1):
        self.model = Word2Vec(self.sentences, vector_size=vector_size, window=window, min_count=min_count, sg=sg)
    
    def vectorize_strings_list(self, strings_list):
        vectors = []
        for word in strings_list:
            if word in self.model.wv:
                vectors.append(self.model.wv[word])
            else:
                vectors.append(np.zeros(self.model.vector_size))
        return np.mean(vectors, axis=0)
    
    def vectorize_method_parameters(self):
        vectors = []
        for method in self.features['method_parameters']:
            method_name, params = method[0], method[1]
            method_vector = self.model.wv[method_name] if method_name in self.model.wv else np.zeros(self.model.vector_size)
            params_vectors = [self.model.wv[param[0]] for param in params if param[0] in self.model.wv]
            if params_vectors:
                params_vector = np.mean(params_vectors, axis=0)
            else:
                params_vector = np.zeros(self.model.vector_size)
            combined_vector = np.concatenate((method_vector, params_vector))
            vectors.append(combined_vector)
        return np.array(vectors)
    
    def combine_vectors(self, vectors):
            return np.mean(vectors, axis=0)
    
    def convert_ndarray_to_list(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.convert_ndarray_to_list(value)
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
    
    def vectorize_features_and_save(self, output_json_path):
        self.load_features_from_json()
        self.extract_string_lists()
        self.train_word2vec_model()
        
        self.features['variable_names_vector'] = self.combine_vectors([self.vectorize_strings_list(sublist) for sublist in self.features['variable_names']])
        self.features['delegate_names_vector'] = self.combine_vectors([self.vectorize_strings_list(sublist) for sublist in self.features['delegate_names']])
        self.features['method_return_types_vector'] = self.combine_vectors([self.vectorize_strings_list(sublist) for sublist in self.features['method_return_types']])
        self.features['method_names_vector'] = self.vectorize_strings_list(self.features['method_names'])
        self.features['class_names_vector'] = self.vectorize_strings_list(self.features['class_names'])
        self.features['interface_names_vector'] = self.vectorize_strings_list(self.features['interface_names'])
        self.features['enums_names_vector'] = self.vectorize_strings_list(self.features['enums_names'])
        self.features['method_parameters_vector'] = self.combine_vectors(self.vectorize_method_parameters())
        
        del self.features['variable_names']
        del self.features['method_names']
        del self.features['class_names']
        del self.features['interface_names']
        del self.features["enums_names"]
        del self.features["delegate_names"]
        del self.features["method_return_types"]
        del self.features["method_parameters"]
        
        self.convert_ndarray_to_list(self.features)
        
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(self.features, f, ensure_ascii=False, indent=4)
        
        print(f'Archivo JSON guardado correctamente en {output_json_path}')

# Ejemplo de uso
if __name__ == "__main__":
    # Ruta al archivo JSON de entrada
    json_file_path = 'data/features_n-omino-main.json'
    
    # Crear una instancia
    fv = FeatureVectorizer(json_file_path)
    fv.vectorize_features_and_save('data/features_vect_n-omino-main.json')