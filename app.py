from flask import Flask, jsonify, request
from flask_cors import CORS
from predict import get_top_plants, filter_by_light, filter_by_soil

app = Flask(__name__)
CORS(app)

# latest sensor readings
latest_data = {
    "temperature": 30,
    "humidity": 60,
    "soil_moisture": 200,
    "light": 20000
}

# =============================
# ESP32 SENSOR DATA ENDPOINT
# =============================

@app.route("/sensor", methods=["POST"])
def sensor():

    global latest_data

    data = request.json

    latest_data = {
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "soil_moisture": data["soil_moisture"],
        "light": data["light"]
    }

    return jsonify({"status":"sensor data received"})


# =============================
# SIMULATE SENSOR DATA
# =============================

@app.route("/simulate")
def simulate():

    global latest_data

    temp = 30
    humidity = 60
    soil_moisture = 210
    lux = 20000

    top_plants = get_top_plants(temp, humidity, soil_moisture)
    light_filtered = filter_by_light(top_plants, lux)
    final_plants = filter_by_soil(light_filtered, soil_moisture)

    latest_data = {
        "temperature": temp,
        "humidity": humidity,
        "soil_moisture": soil_moisture,
        "light": lux,
        "ml_recommendations": top_plants,
        "final_recommendations": final_plants
    }

    return jsonify(latest_data)


# =============================
# DASHBOARD FETCHES DATA HERE
# =============================

@app.route("/data")
def data():
    return jsonify(latest_data)


# =============================
# PLANT RECOMMENDATION API
# =============================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    temp = data["temperature"]
    humidity = data["humidity"]
    soil_moisture = data["soil_moisture"]
    lux = data["light_intensity"]

    top_plants = get_top_plants(temp, humidity, soil_moisture)
    light_filtered = filter_by_light(top_plants, lux)
    final_plants = filter_by_soil(light_filtered, soil_moisture)

    return jsonify({
        "ml_recommendations": top_plants,
        "final_recommendations": final_plants
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)