#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Nishant";
const char* password = "nishantsharma";

// Replace with your laptop IP running Flask
String serverName = "http://172.20.10.14:5000/sensor";

// Sensor pins
int soilPin = 32;
int lightPin = 26;

void setup() {

  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
}

void loop() {

  int soilValue = analogRead(soilPin);
  int lightValue = analogRead(lightPin);

  // Fake values if you don't have sensors connected yet
  float temperature = 28;
  float humidity = 65;

  Serial.println("Sending sensor data");

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String json = "{";
    json += "\"temperature\":" + String(temperature) + ",";
    json += "\"humidity\":" + String(humidity) + ",";
    json += "\"soil_moisture\":" + String(soilValue) + ",";
    json += "\"light\":" + String(lightValue);
    json += "}";

    int responseCode = http.POST(json);

    Serial.print("Response: ");
    Serial.println(responseCode);

    http.end();
  }

  delay(5000);
}