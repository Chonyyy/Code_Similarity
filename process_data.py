import json
import pandas as pd

# Cargar el JSON
with open('path/to/your/feature_extractor_output.json', 'r') as f:
    data = json.load(f)

# Convertir a DataFrame
df = pd.DataFrame([data])
print(df.head())
