import os, random
import tensorflow as tf
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Input, Lambda
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from keras.layers import Input, Lambda, Dense, Dropout, Flatten,Activation, Flatten, Reshape
import numpy as np
from tensorflow.keras.layers import Layer
import tensorflow.keras.backend as K
from siamese_network_parse import PrepareDataSNN
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from tensorflow.keras.initializers import GlorotUniform
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.losses import binary_crossentropy

# Configurar la semilla para reproducibilidad
# SEED = 44


class SiameseNeuralNetwork:
    def __init__(self, input_shape, learning_rate=0.001, SEED=37):
        self.input_shape = input_shape
        self.learning_rate = learning_rate
        self.l2_reg = 0.2
        self.SEED = SEED
        tf.random.set_seed(self.SEED)
        np.random.seed(self.SEED)
        random.seed(self.SEED)
        self.model = self._build_model()
    
    def create_base_network(self, input_shape):
        model = Sequential()
        initializer = GlorotUniform(seed=self.SEED)

        model.add(Dense(512, activation="relu", input_shape=input_shape, kernel_initializer=initializer))
        model.add(BatchNormalization())  # Normalización por lotes
        model.add(Dropout(0.5))
        model.add(Dense(256, activation="relu", kernel_initializer=initializer))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        model.add(Dense(128, activation="relu", kernel_initializer=initializer))
        model.add(BatchNormalization()) 

        return model

    def _build_model(self):
        # Red base
        base_network = self.create_base_network(self.input_shape)

        # Entradas
        input_a = Input(shape=self.input_shape)
        input_b = Input(shape=self.input_shape)

        # Representaciones aprendidas
        encoded_a = base_network(input_a)
        encoded_b = base_network(input_b)

        # Distancia L1 con `output_shape`
        l1_distance = L1Distance()([encoded_a, encoded_b])

        # Clasificación binaria
        output = Dense(1, activation='sigmoid')(l1_distance)

        # Modelo completo
        model = Model(inputs=[input_a, input_b], outputs=output)
        model.compile(loss='binary_crossentropy', optimizer=Adam(self.learning_rate), metrics=['accuracy'])
        # model.compile(loss=asymmetric_loss, optimizer=Adam(self.learning_rate), metrics=['accuracy'])
        return model
     
    def euclidean_distance(self, vects):
        x, y = vects
        sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
        return K.sqrt(K.maximum(sum_square, K.epsilon()))

    def _save_model(self, model_name):
        """Guarda el modelo"""

        # Deshabilitar el modo seguro para deserializar funciones lambda
        tf.keras.config.enable_unsafe_deserialization()
        if not os.path.exists('./models'):
            os.makedirs('./models')
        self.model.save(f'models/{model_name}.keras')

    def train(self, X1_train, X2_train, y_train, validation_data, epochs=20, batch_size=32):
        X1_val, X2_val, y_val = validation_data
        history = self.model.fit([X1_train, X2_train], y_train,
                                 validation_data=([X1_val, X2_val], y_val),
                                 epochs=epochs, 
                                 batch_size=batch_size,
                                 shuffle=False)
        return history

    def predict_similarity(self, code1_features, code2_features):
        """Predice la similitud entre dos fragmentos de código"""
        
        code1_features = np.array(code1_features).reshape(1, -1)
        code2_features = np.array(code2_features).reshape(1, -1)
        return self.model.predict([code1_features, code2_features])[0][0]
    
    def find_duplicates_from_folder(self, folder_path, threshold=0.35):
        """
        Encuentra pares de proyectos que son considerados copias entre sí.

        Retorna:
        - duplicates: Lista de pares de proyectos considerados copias.
        """
        data_a, data_b, labels, names = PrepareDataSNN(folder_path, predict=True).process()

        duplicates = []
        count = 0
        # Comparar cada par de proyectos
        for a, b, name in zip(data_a, data_b, names):
        
                similarity = self.predict_similarity(a, b)

                # Verificar si excede el umbral
                if similarity >= threshold:
                    duplicates.append(name)
                    count += 1 
                    print(f"¡Posibles copias detectadas!: {name} (Similitud: {similarity:.2f})")

        print(f"Cantidad de copias {count}:\n {duplicates}")
        return duplicates


    def evaluate(self, data_a, data_b, labels, pairs=None):
        # Evaluar la pérdida y la precisión
        loss, accuracy = self.model.evaluate([data_a, data_b], labels, verbose=1)
        print(f"Pérdida en los nuevos datos: {loss:.4f}")
        print(f"Accuracy en los nuevos datos: {accuracy:.4f}")
        
        # Generar predicciones con un umbral ajustado
        threshold = 0.20  # Ajusta este valor según los resultados que obtengas
        predictions = (self.model.predict([data_a, data_b]) > threshold).astype(int).flatten()
        
        # Calcular la matriz de confusión
        tn, fp, fn, tp = confusion_matrix(labels, predictions).ravel()
        
        # Calcular métricas adicionales
        precision = precision_score(labels, predictions)
        recall = recall_score(labels, predictions)
        f1 = f1_score(labels, predictions)
        
        # Imprimir las métricas adicionales
        print(f"Verdaderos Positivos (TP): {tp}")
        print(f"Falsos Positivos (FP): {fp}")
        print(f"Verdaderos Negativos (TN): {tn}")
        print(f"Falsos Negativos (FN): {fn}")
        print(f"Precisión (Precision): {precision:.4f}")
        print(f"Exhaustividad (Recall): {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")

        # Registrar pares que resultaron en FN y VP
        falsos_negativos = []
        falsos_positivos = []
        verdaderos_positivos = []
        
        if pairs is not None:
            for pair, true, pred in zip(pairs, labels, predictions):
                if true == 1 and pred == 0:
                    falsos_negativos.append(pair)
                elif true == 0 and pred == 1:
                    falsos_positivos.append(pair)
                elif true == 1 and pred == 1:
                    verdaderos_positivos.append(pair)

            print("\nFalsos negativos:")
            for fn_pair in falsos_negativos:
                print(f"Par: {fn_pair}")

            print("\nFalsos positivos:")
            for fp_pair in falsos_positivos:
                print(f"Par: {fp_pair}")

            print("\nVerdaderos positivos:")
            for vp_pair in verdaderos_positivos:
                print(f"Par: {vp_pair}")
        
        # Retornar resultados
        metrics = {
            "loss": loss,
            "accuracy": accuracy,
            "tp": tp,
            "fp": fp,
            "tn": tn,
            "fn": fn,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }
        return metrics

def asymmetric_loss(y_true, y_pred):
    """
    Función de pérdida con penalización asimétrica para falsos negativos.
    
    Parámetros:
    - y_true: Etiquetas reales (0 o 1).
    - y_pred: Predicciones del modelo (probabilidades entre 0 y 1).
    
    Retorna:
    - Valor escalar de la pérdida modificada.
    """
    alpha = 5  # Factor de penalización para falsos negativos (ajustar según necesidad)

    # Pérdida binaria estándar
    base_loss = binary_crossentropy(y_true, y_pred)

    # Penalización para falsos negativos
    penalization = alpha * y_true * K.log(1 - y_pred + K.epsilon())

    # Pérdida total
    loss = base_loss - penalization
    return loss

class L1Distance(Layer):
    def __init__(self, **kwargs):
        super(L1Distance, self).__init__(**kwargs)

    def call(self, tensors):
        x, y = tensors
        return K.abs(x - y)

if __name__ == "__main__":

    data = PrepareDataSNN()

    # Ruta para guardar los datos
    data_dir = "./data_snn"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    data_file = os.path.join(data_dir, "dataset_split.npz")

    # if os.path.exists(data_file):
    #     # Cargar los datos si ya están guardados
    #     print("Cargando conjuntos de entrenamiento y validación desde archivo...")
    #     data = np.load(data_file)
    #     X1_train, X1_val = data["X1_train"], data["X1_val"]
    #     X2_train, X2_val = data["X2_train"], data["X2_val"]
    #     y_train, y_val = data["y_train"], data["y_val"]
    # else:
    #     # Crear los conjuntos de datos y guardarlos
    #     print("Dividiendo los datos y guardándolos...")
    #     data_a, data_b, labels, names = PrepareDataSNN().process()
    #     X1_train, X1_val, X2_train, X2_val, y_train, y_val = train_test_split(
    #         data_a, data_b, labels, test_size=0.2, random_state=42
    #     )
    #     np.savez(data_file, X1_train=X1_train, X1_val=X1_val, 
    #              X2_train=X2_train, X2_val=X2_val, 
    #              y_train=y_train, y_val=y_val)

    if os.path.exists(data_file):
        print("Cargando conjuntos de datos...")
        data = np.load(data_file)
        X1_train, X1_val, X1_test = data["X1_train"], data["X1_val"], data["X1_test"]
        X2_train, X2_val, X2_test = data["X2_train"], data["X2_val"], data["X2_test"]
        y_train, y_val, y_test = data["y_train"], data["y_val"], data["y_test"]
    else:
        print("Procesando y dividiendo los datos...")
        data_a, data_b, labels, names = PrepareDataSNN().process()

        X1_temp, X1_test, X2_temp, X2_test, y_temp, y_test = train_test_split(
            data_a, data_b, labels, test_size=0.2, random_state=42
        )

        X1_train, X1_val, X2_train, X2_val, y_train, y_val = train_test_split(
            X1_temp, X2_temp, y_temp, test_size=0.25, random_state=42
        )

        np.savez(data_file, 
                 X1_train=X1_train, X2_train=X2_train, y_train=y_train,
                 X1_val=X1_val, X2_val=X2_val, y_val=y_val,
                 X1_test=X1_test, X2_test=X2_test, y_test=y_test)


    # Datos de validacion
    # data_dir = "./data_val"
    # if not os.path.exists(data_dir):
    #     os.makedirs(data_dir)
    # data_file = os.path.join(data_dir, "dataset_split.npz")

    # if os.path.exists(data_file):
    #     # Cargar los datos si ya están guardados
    #     print("Cargando conjuntos de validación desde archivo...")
    #     data = np.load(data_file)
    #     X1_new, X2_new, y_new, names = data["X1_new"], data["X2_new"], data["y_new"], data["names"]
    # else:
    #     print("Procesando los datos de validación y guardándolos...")
    #     data_val = PrepareDataSNN("data/features_vect_val/")
    #     X1_new, X2_new, y_new, names = data_val.process()
        
    #     # Guardar los datos procesados
    #     np.savez(data_file, X1_new=X1_new, X2_new=X2_new, y_new=y_new, names=names)

    # # Verificar las formas de los arrays
    # print("Formas de los conjuntos de validación:")
    # print(f"X1_new: {X1_new.shape}")
    # print(f"X2_new: {X2_new.shape}")
    # print(f"y_new: {y_new.shape}")

    # # Inicializar y entrenar la red
    # input_shape = (65,)  # Asumiendo que tus vectores de características tienen 65 elementos
    # siamese_net = SiameseNeuralNetwork(input_shape)
    # history = siamese_net.train(X1_train, X2_train, y_train, validation_data=(X1_val, X2_val, y_val))

    # # Guardar el modelo
    # # siamese_net._save_model("model_1")


    # m = siamese_net.evaluate(X1_new, X2_new, y_new, names)


    # siamese_net.find_duplicates_from_folder("data/features_vect_val")

    # Hacer una predicción
    # code1_features = np.random.rand(65)  # Ejemplo de vector de características
    # code2_features = np.random.rand(65)  # Ejemplo de vector de características
    
    # similarity = siamese_net.predict_similarity(code1_features, code1_features)

    # print(f"La similitud entre los dos códigos es: {similarity}")



    input_shape = (65,)
    siamese_net = SiameseNeuralNetwork(input_shape)

    print("Entrenando el modelo...")
    history = siamese_net.train(X1_train, X2_train, y_train, validation_data=(X1_val, X2_val, y_val))

    print("Evaluando en el conjunto de prueba...")
    metrics = siamese_net.evaluate(X1_test, X2_test, y_test)
    print(f"Métricas en el conjunto de prueba: {metrics}")

