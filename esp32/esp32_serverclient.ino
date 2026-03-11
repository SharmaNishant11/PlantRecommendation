#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI_NAME"; // replace with your WiFi SSID
const char* password = "YOUR_WIFI_PASSWORD"; // replace with your WiFi password

String serverName = "http://YOUR_PC_IP:5000/predict"; // replace with your PC's IP address and Flask endpoint
 
// sensor pins
// replace with your actual sensor pins
int lightPin = 34; 
int soilPin = 35;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
}

void loop() {

  int lightValue = analogRead(lightPin);
  int soilValue = analogRead(soilPin);

  Serial.print("Light: ");
  Serial.println(lightValue);

  Serial.print("Soil: ");
  Serial.println(soilValue);

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    // replace temperature and humidity with actual sensor values if you have them
    String jsonData = "{";
    jsonData += "\"temperature\":30,";
    jsonData += "\"humidity\":60,";
    jsonData += "\"soil_moisture\":" + String(soilValue) + ",";
    jsonData += "\"light_intensity\":" + String(lightValue);
    jsonData += "}";

    int httpResponseCode = http.POST(jsonData);

    Serial.print("HTTP Response: ");
    Serial.println(httpResponseCode);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Server Response:");
      Serial.println(response);
    }

    http.end();
  }

  delay(10000); // send every 10 seconds
}