import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score





DATASET_PATH = os.path.join("Datasets", "Crop_recommendation.csv")

data = pd.read_csv(DATASET_PATH)
print(data.head())

# Keep only relevant columns
df = data[['Temperature', 'Humidity', 'Rainfall', 'Crop']]

# Rename Rainfall → SoilMoistureProxy (important for report clarity)
df = df.rename(columns={'Rainfall': 'SoilMoisture'})

le = LabelEncoder()
df['PlantLabel'] = le.fit_transform(df['Crop'])

def estimate_sunlight(row):
    if row['Temperature'] > 30 and row['Humidity'] < 50:
        return 2  # High
    elif row['Temperature'] > 20:
        return 1  # Medium
    else:
        return 0  # Low

df['Sunlight'] = df.apply(estimate_sunlight, axis=1)
X = df[['SoilMoisture', 'Sunlight', 'Humidity', 'Temperature']]
y = df['PlantLabel']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=6)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))
