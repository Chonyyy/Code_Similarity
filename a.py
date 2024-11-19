import os
import tensorflow as tf
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Input, Lambda
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from keras.layers import Input, Lambda, Dense, Dropout, Convolution2D,Conv1D, MaxPooling2D, Flatten,Activation, Flatten, Reshape, Conv1D, MaxPooling1D
import numpy as np
import tensorflow.keras.backend as K
from SNN.siamese_network_parse import PrepareDataSNN
from sklearn.model_selection import train_test_split

import numpy as np

class SiameseNeuralNetwork:
    def __init__(self, input_shape,l2_regularization_penalization = 0.01, learning_rate=0.001):
        self.input_shape = input_shape
        self.learning_rate = learning_rate
        self.l2_reg = l2_regularization_penalization
        self.model = self._build_model_l1_distance()
    
    def create_base_network(self, input_shape):
        model = Sequential()
        
        # Reshape the input to be compatible with Conv1D
        model.add(Reshape((65, 1), input_shape=input_shape))
        
        # Replace Convolution2D with Conv1D
        model.add(Conv1D(16, 8, strides=1, activation="relu"))
        model.add(MaxPooling1D(pool_size=2))
        
        model.add(Conv1D(32, 4, strides=1, activation="relu"))
        model.add(MaxPooling1D(pool_size=2))
        
        model.add(Flatten())
        model.add(Dense(512, activation="relu"))
        model.add(Dense(256, activation="relu"))
        model.add(Dense(10, activation='softmax'))

        return model

    def create_base_network_l1_distance(self, input_shape):
        model = Sequential()
        
        # Reshape the input to be compatible with Conv1D
        model.add(Reshape((65, 1), input_shape=input_shape))
        
        # Replace Convolution2D with Conv1D
        model.add(Conv1D(16, 8, strides=1, activation="relu"))
        model.add(MaxPooling1D(pool_size=2))
        
        model.add(Conv1D(32, 4, strides=1, activation="relu"))
        model.add(MaxPooling1D(pool_size=2))
        
        model.add(Flatten())
        model.add(Dense(512, activation="relu", kernel_regularizer=l2(self.l2_reg)))
        model.add(Dense(256, activation="relu", kernel_regularizer=l2(self.l2_reg)))
        model.add(Dense(10, activation='softmax', kernel_regularizer=l2(self.l2_reg)))

        return model


    def _build_model(self):
        # Definir la red base
        base_network = self.create_base_network(input_shape)

        # Definir el modelo siamés
        input_a = Input(shape=self.input_shape)
        input_b = Input(shape=self.input_shape)

        encoded_a = base_network(input_a)
        encoded_b = base_network(input_b)

        # Capa de distancia
        distance = Lambda(self.euclidean_distance, output_shape=(1,))([encoded_a, encoded_b])

        # Capa de salida
        output = Dense(1, activation='sigmoid')(distance)

        model = Model(inputs=[input_a, input_b], outputs=output)
        model.compile(loss='binary_crossentropy', optimizer=Adam(self.learning_rate), metrics=['accuracy'])
        return model
    
    def _build_model_l1_distance(self):
        #Definimos la red base
        base_network = self.create_base_network_l1_distance(input_shape)

        # Entradas para los pares de códigos
        input_code_1 = Input(self.input_shape)
        input_code_2 = Input(self.input_shape)

        # Codificamos ambos códigos
        encoded_code_1 = base_network(input_code_1)
        encoded_code_2 = base_network(input_code_2)

        # Capa de distancia L1
        l1_distance = Lambda(lambda tensors: tf.abs(tensors[0] - tensors[1]))
        l1_distance_layer = l1_distance([encoded_code_1, encoded_code_2])

        # Predicción de similitud
        prediction = Dense(1, activation='sigmoid')(l1_distance_layer)

        self.model = Model(inputs=[input_code_1, input_code_2], outputs=prediction)

        optimizer = Adam(learning_rate=self.learning_rate)
        self.model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        return self.model
    
    def euclidean_distance(self, vects):
        x, y = vects
        sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
        return K.sqrt(K.maximum(sum_square, K.epsilon()))


    def _save_model(self, model_name):
        """Guarda el modelo"""
        if not os.path.exists('./models'):
            os.makedirs('./models')
        self.model.save(f'models/{model_name}.h5')

    def train(self, data_a, data_b, labels, validation_data=None, epochs=20, batch_size=32):
        if validation_data:
            X1_val, X2_val, y_val = validation_data
            history = self.model.fit([data_a, data_b], labels, 
                                    validation_data=([X1_val, X2_val], y_val),
                                    epochs=epochs, 
                                    batch_size=batch_size)
        else:
            history = self.model.fit([data_a, data_b], labels, 
                                    validation_split=0.2,
                                    epochs=epochs, 
                                    batch_size=batch_size)
        return history

    def predict_similarity(self, code1_features, code2_features):
        """Predice la similitud entre dos fragmentos de código"""
        # Asegurarse de que las características tengan la forma correcta
        code1_features = np.array(code1_features).reshape(1, -1)
        code2_features = np.array(code2_features).reshape(1, -1)
        
        return self.model.predict([code1_features, code2_features])[0][0]

# Asumiendo que ya tienes tus datos procesados
data = PrepareDataSNN()
data_a, data_b, labels = data.process()

# Dividir los datos en conjuntos de entrenamiento y validación
X1_train, X1_val, X2_train, X2_val, y_train, y_val = train_test_split(
    data_a, data_b, labels, test_size=0.2, random_state=42
)

# Ahora tienes:
# X1_train, X2_train, y_train: Datos de entrenamiento
# X1_val, X2_val, y_val: Datos de validación

# Verificar las formas de los arrays
print("Formas de los conjuntos de entrenamiento:")
print(f"X1_train: {X1_train.shape}")
print(f"X2_train: {X2_train.shape}")
print(f"y_train: {y_train.shape}")

print("\nFormas de los conjuntos de validación:")
print(f"X1_val: {X1_val.shape}")
print(f"X2_val: {X2_val.shape}")
print(f"y_val: {y_val.shape}")


# Inicializar y entrenar la red
input_shape = (65,)  # Asumiendo que tus vectores de características tienen 65 elementos
siamese_net = SiameseNeuralNetwork(input_shape)
history = siamese_net.train(X1_train, X2_train, y_train, validation_data=(X1_val, X2_val, y_val))

# Hacer una predicción
code1_features = np.random.rand(65)  # Ejemplo de vector de características
code2_features = np.random.rand(65)  # Ejemplo de vector de características
similarity = siamese_net.predict_similarity(code1_features, code2_features)

# Interpretar el resultado
if similarity > 0.5:
    print(f"Los códigos son similares con una probabilidad de {similarity:.2f}")
else:
    print(f"Los códigos son diferentes con una probabilidad de {1-similarity:.2f}")

print(f"La similitud entre los dos códigos es: {similarity:.4f}")

