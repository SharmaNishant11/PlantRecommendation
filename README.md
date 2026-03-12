# 🌱 PlantRec – Smart Plant Recommendation System

An **IoT + Machine Learning + Web Dashboard** system that recommends plants based on environmental conditions such as **soil moisture, temperature, humidity, and sunlight**.

The system collects real-time sensor data using an **ESP32/Arduino**, processes it through a **Random Forest ML model**, and displays recommendations on a **web dashboard**.

---

# 🚀 Features

• Real-time sensor monitoring  
• Machine Learning plant recommendations  
• Web dashboard visualization  
• Live sensor graphs  
• Environmental data storage  
• ESP32 IoT integration  

---

# 🧠 Technologies Used

| Component | Technology |
|--------|--------|
| Backend API | Flask |
| Machine Learning | Scikit-learn |
| Model | Random Forest |
| Hardware | ESP32 / Arduino |
| Sensors | Soil Moisture + Light |
| Dashboard | HTML + CSS + JavaScript |


---

# 📂 Project Structure
PlantRec
│
├── datasets
│
├── model
│ └── plant_model.pkl
│
├── esp32
│ └── esp32_sensor_client.ino
│
├── dashboard
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── app.py
├── predict.py
├── train.py
│
├── requirements.txt
├── Dockerfile
└── README.md


---

# ⚙️ Installation

## 1 Install dependencies


pip install -r requirements.txt


---

## 2 Train the model


python train.py


This generates:


model/plant_model.pkl


---

## 3 Run the server


python app.py


Flask server will start:


http://localhost:5000


---

## 4 Open the dashboard

Open:


dashboard/index.html


in your browser.

---

# 📡 ESP32 Setup

Update the ESP32 code:


String serverName = "http://YOUR_PC_IP:5000/sensor";


Upload the code to your ESP32.

Sensor data will automatically stream to the server.

---

# 📊 Dashboard

The dashboard displays:

• Temperature  
• Soil moisture  
• Light intensity  
• Live sensor graphs  
• Recommended plants  

---

# 🤖 Machine Learning Model

The model is trained using the **Crop Recommendation dataset**.

Input features:


temperature
humidity
soil moisture
light intensity


Model:


RandomForestClassifier


Output:


Top recommended crops/plants


---

# 🐳 Docker (Optional)

Build container:


docker build -t plantrec .


Run:


docker run -p 5000:5000 plantrec


---

# 🧪 Example API Request


POST /predict

{
"temperature": 30,
"humidity": 60,
"soil_moisture": 300,
"light_intensity": 20000
}


Response:


{
"ml_recommendations": ["coffee","blackgram","pigeonpeas"],
"final_recommendations": ["coffee"]
}


---

# 🌿 Future Improvements

• Sunlight heatmap mapping  
• Automated irrigation suggestions  
• Camera-based plant health detection  
• Mobile app integration  

---

