from flask import Flask, request, jsonifypyth
from flask_cors import CORS
from predict import get_top_plants, filter_by_light, filter_by_soil

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

# store latest data for dashboard
latest_sensor_data = {}
latest_predictions = {}

@app.route("/predict", methods=["POST"])
def predict():
    global latest_sensor_data
    global latest_predictions

    data = request.json

    temp = data["temperature"]
    humidity = data["humidity"]
    soil_moisture = data["soil_moisture"]
    lux = data["light_intensity"]

    top_plants = get_top_plants(temp, humidity, soil_moisture)
    light_filtered = filter_by_light(top_plants, lux)
    final_plants = filter_by_soil(light_filtered, soil_moisture)

    latest_sensor_data = data
    latest_predictions = {
        "ml_recommendations": top_plants,
        "final_recommendations": final_plants
    }

    return jsonify(latest_predictions)


# NEW endpoint for dashboard
@app.route("/data")
def get_data():
    return jsonify({
        "sensor": latest_sensor_data,
        "predictions": latest_predictions
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)