import os
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from SNN.siamese_network import L1Distance
from SNN.siamese_network_parse import PrepareDataSNN
from test_ast_for_each_arch import ProjectFeatureProcessor

class SimilarityDetector:
    def __init__(self, projects_folder, data_folder, data_folder_vect, model_path, threshold=0.30):
        self.projects_folder = projects_folder
        self.data_folder = data_folder
        self.data_folder_vect = data_folder_vect
        self.model_path = model_path
        self.threshold = threshold
        self.processor = ProjectFeatureProcessor(projects_folder, data_folder, data_folder_vect)
        self.model = load_model(self.model_path, custom_objects={'L1Distance': L1Distance})

    def process_projects(self):
        """Procesa los proyectos para generar características."""
        self.processor.process_projects()

    def predict_similarity(self, code1_features, code2_features):
        """Predice la similitud entre dos fragmentos de código."""
        code1_features = np.array(code1_features).reshape(1, -1)
        code2_features = np.array(code2_features).reshape(1, -1)
        return self.model.predict([code1_features, code2_features])[0][0]

    def detect_duplicates(self):
        """Detecta posibles duplicados entre proyectos."""
        data_a, data_b, labels, names = PrepareDataSNN(self.data_folder_vect, predict=True).process()

        duplicates = []
        count = 0

        for a, b, name in zip(data_a, data_b, names):
            similarity = self.predict_similarity(a, b)

            if similarity >= self.threshold:
                duplicates.append(name)
                count += 1
                print(f"¡Posibles copias detectadas!: {name} (Similitud: {similarity:.2f})")

        print(f"Cantidad de copias {count}:{duplicates}")
        return duplicates, count

if __name__ == "__main__":
    PROJECTS_FOLDER = f"{os.getcwd()}/Projects/pruebas/Moogle/"
    DATA_FOLDER = f"{os.getcwd()}/data/pruebas/Moogle/features"
    DATA_FOLDER_VECT = f"{os.getcwd()}/data/pruebas/Moogle/features_vect"
    MODEL_PATH = "./models/model_1.keras"

    detector = SimilarityDetector(PROJECTS_FOLDER, DATA_FOLDER, DATA_FOLDER_VECT, MODEL_PATH)

    # Procesar proyectos y cargar el modelo
    detector.process_projects()

    detector.detect_duplicates()
