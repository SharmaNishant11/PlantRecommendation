import joblib
import numpy as np
import pandas as pd

light_db = pd.read_csv("Datasets/plant_light_requirements.csv")

def classify_light(lux):
    if lux < 10000:
        return "low"
    elif lux < 40000:
        return "medium"
    else:
        return "high"

def filter_by_light(plants, lux_value):
    sensor_light = classify_light(lux_value)
    filtered = []

    light_levels = {"low": 1, "medium": 2, "high": 3}

    for plant in plants:
        required = light_db[light_db["plant"] == plant]["light_requirement"].values

        if len(required) > 0:
            if light_levels[sensor_light] >= light_levels[required[0]]:
                filtered.append(plant)

    if not filtered:
        return plants

    return filtered

# Load model
model = joblib.load("plant_model.pkl")

def get_top_plants(temp, humidity, soil_moisture):
    input_df = pd.DataFrame(
        [[temp, humidity, soil_moisture]],
        columns=["temperature", "humidity", "soil_moisture"]
    )

    probabilities = model.predict_proba(input_df)[0]
    
    top_indices = np.argsort(probabilities)[-3:]
    top_plants = model.classes_[top_indices]
    
    return list(top_plants)


# Example full pipeline test
if __name__ == "__main__":
    temp = 30
    humidity = 70
    soil_moisture = 200
    lux = 45000

    top_plants = get_top_plants(temp, humidity, soil_moisture)
    final_plants = filter_by_light(top_plants, lux)

    print("ML Recommendations:", top_plants)
    print("Final After Light Filter:", final_plants)