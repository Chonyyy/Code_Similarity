import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def prepare_dataset(files):
    features = []
    labels = []
    for file, label in files:
        file_features = extract_features_from_file(file)
        features.append(file_features)
        labels.append(label)
    df = pd.DataFrame(features)
    df['label'] = labels
    return df

# Lista de archivos y sus etiquetas correspondientes (ejemplo)
files = [
    ('file1.cs', 'fraud'),
    ('file2.cs', 'non-fraud'),
    # Agrega más archivos y etiquetas
]

dataset = prepare_dataset(files)

# Separar en conjunto de entrenamiento y prueba

X = dataset.drop(columns=['label'])
y = dataset['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
