import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("datasets/Crop_recommendation.csv")

# Rename rainfall to soil_moisture
data = data.rename(columns={"rainfall": "soil_moisture"})

# Select features
X = data[["temperature", "humidity", "soil_moisture"]]
y = data["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
accuracy = accuracy_score(y_test, model.predict(X_test))
print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "plant_model.pkl")