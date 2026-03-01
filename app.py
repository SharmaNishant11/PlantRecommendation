from flask import Flask, request, jsonify
from predict import get_top_plants, filter_by_light, filter_by_soil

app = Flask(__name__)

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
    app.run(debug=True)