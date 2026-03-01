import joblib
import numpy as np

# Load model
model = joblib.load("plant_model.pkl")

def get_top_plants(temp, humidity, soil_moisture):
    input_data = np.array([[temp, humidity, soil_moisture]])
    
    probabilities = model.predict_proba(input_data)[0]
    
    top_indices = np.argsort(probabilities)[-3:]
    top_plants = model.classes_[top_indices]
    
    return list(top_plants)

# Example test
print(get_top_plants(30, 70, 200))