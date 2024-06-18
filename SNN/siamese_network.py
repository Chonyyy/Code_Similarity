import itertools
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Lambda, Subtract
from tensorflow.keras.optimizers import Adam
import tensorflow.keras.backend as K
from siamese_network_parse import generate_pairs
import json

json_file = "data/training_pairs_SNN/training_pairs.json"

# Función para crear el modelo siamés
def create_siamese_model(input_shape):
    input_a = Input(shape=input_shape)
    input_b = Input(shape=input_shape)
    
    dense_layer = Dense(128, activation='relu')
    encoded_a = dense_layer(input_a)
    encoded_b = dense_layer(input_b)
    
    distance = Lambda(lambda tensors: K.abs(tensors[0] - tensors[1]))([encoded_a, encoded_b])
    
    prediction = Dense(1, activation='sigmoid')(distance)
    
    model = Model(inputs=[input_a, input_b], outputs=prediction)
    
    return model



data = pd.read_json(json_file)
    
# Dividir en conjuntos de entrenamiento y prueba
pairs_train, pairs_test = train_test_split(data, test_size=0.2, random_state=42)
    
# Definir forma de entrada
input_shape = data.shape  # Ajusta según tus datos

# Crear el modelo siamés
model = create_siamese_model(input_shape)

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

# Preparar los datos para entrenamiento
pairs_train_input = [np.array([pair["project_1"] for pair in pairs_train]), np.array([pair["project_2"] for pair in pairs_train])]
labels_train = np.array([pair["similarity_flag"] for pair in pairs_train])

# Entrenar el modelo
model.fit(pairs_train_input, labels_train, batch_size=32, epochs=10)

# Evaluar el modelo
pairs_test_input = [np.array([pair["project_1"] for pair in pairs_test]), np.array([pair["project_2"] for pair in pairs_test])]
labels_test = np.array([pair["similarity_flag"] for pair in pairs_test])

loss, accuracy = model.evaluate(pairs_test_input, labels_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')

# Guardar el modelo entrenado si se desea
model.save('siamese_model.h5')