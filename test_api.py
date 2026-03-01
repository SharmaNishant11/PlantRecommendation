import requests

data = {
    "temperature": 30,
    "humidity": 70,
    "soil_moisture": 200,
    "light_intensity": 45000
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)

print(response.json())