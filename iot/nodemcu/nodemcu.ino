#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Thông số WiFi và MQTT
const char* ssid = "phong02468";
const char* wifiPassword = "12481632";
const char* mqtt_server = "192.168.137.244";

// Định danh cho xe đạp và chỗ đỗ xe
const char* localBikeId = "123";
const char* localParkingSlotId = "3"; // Định danh chỗ đỗ xe

// Chân nút nhấn
const int buttonPin = D0; // Chọn chân D0 cho nút nhấn

WiFiClient espClient;
PubSubClient client(espClient);

// Các chân kết nối RGB LED cho XE ĐẠP
const int pinR = D5;
const int pinG = D6;
const int pinB = D7;

// Các chân kết nối RGB LED cho CHỖ ĐỂ XE
const int pinParkingR = D2;
const int pinParkingG = D3;
const int pinParkingB = D4;

// Chân loa
const int speakerPin = D1;

// Biến debounce cho nút nhấn
unsigned long lastButtonPress = 0;
const unsigned long buttonDebounceDelay = 50; // 50ms debounce

void callback(char* topic, byte* payload, unsigned int length) {
    // ... (phần code callback hiện tại của bạn) ...
    String topicStr = String(topic);

    // **Xử lý topic điều khiển xe đạp (bike/status/<bikeId>)**
    if (topicStr.startsWith("bike/status/")) {
        // ... (code xử lý bike status hiện tại) ...
        // Lấy bikeId từ topic
        int slashIndex = topicStr.lastIndexOf('/');
        String topicBikeId = topicStr.substring(slashIndex + 1);

        // Kiểm tra xem thông điệp có dành cho xe này không
        if (topicBikeId == String(localBikeId)) {
            char msg[150];
            if (length < sizeof(msg)) {
                memcpy(msg, payload, length);
                msg[length] = '\0';
            } else {
                return;
            }

            // **CHỈNH SỬA ĐÂY: Thêm kích thước cho JsonDocument**
            JsonDocument doc;
            DeserializationError error = deserializeJson(doc, msg);
            if (error) {
                Serial.println("Deserialize JSON (Bike) failed");
                return;
            }

            const char* status = doc["status"];
            Serial.print("Bike ");
            Serial.print(localBikeId);
            Serial.print(" received status: ");
            Serial.println(status);

            if (strcmp(status, "borrowed") == 0) {
                // Màu đỏ cho trạng thái "mượn" (Bike)
                analogWrite(pinR, 0);
                analogWrite(pinG, 255);
                analogWrite(pinB, 255);
                for (int i = 0; i < 4; i++) {
                    tone(speakerPin, 2731, 200);
                    delay(300);
                }
            } else if (strcmp(status, "returned") == 0) {
                // Màu xanh lá cho trạng thái "trả" (Bike)
                analogWrite(pinR, 255);
                analogWrite(pinG, 0);
                analogWrite(pinB, 255);
                for (int i = 0; i < 2; i++) {
                    tone(speakerPin, 3000, 200);
                    delay(300);
                }
            } else if (strcmp(status, "maintenance") == 0) {
                // Màu vàng cho trạng thái "bảo trì" (Bike)
                analogWrite(pinR, 0);
                analogWrite(pinG, 0);
                analogWrite(pinB, 255);
                tone(speakerPin, 4000, 180000);
            } else {
                // Tắt LED (Bike)
                analogWrite(pinR, 255);
                analogWrite(pinG, 255);
                analogWrite(pinB, 255);
                noTone(speakerPin);
            }
        }
    }

    // **Xử lý topic điều khiển chỗ đỗ xe (parking/command)**
    else if (topicStr.startsWith("parking/command")) {
        // ... (code xử lý parking command hiện tại) ...
        char msg[200]; // Tăng kích thước buffer
        if (length < sizeof(msg)) {
            memcpy(msg, payload, length);
            msg[length] = '\0';
        } else {
            Serial.println("Payload (Parking) quá dài!");
            return;
        }

        // **CHỈNH SỬA ĐÂY: Thêm kích thước cho JsonDocument**
        JsonDocument doc;
        DeserializationError error = deserializeJson(doc, msg);
        if (error) {
            Serial.println("Deserialize JSON (Parking) failed");
            Serial.println(error.c_str());
            return;
        }

        const char* command = doc["command"];
        if (command == nullptr) {
            Serial.println("Không tìm thấy 'command' trong JSON payload (Parking)!");
            return;
        }

        Serial.print("Parking Slot received command: ");
        Serial.println(command);

        if (strcmp(command, "unlock") == 0 || strcmp(command, "available") == 0 || strcmp(command, "vacant") == 0) {
            // Màu xanh lá cây cho trạng thái "trống/sẵn sàng" (Parking)
            analogWrite(pinParkingR, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingG, 0);    // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingB, 255); // CHỈNH SỬA ĐÂY
            Serial.println("Set LED to Green (Parking - Available)");
        } else if (strcmp(command, "lock") == 0 || strcmp(command, "occupied") == 0) {
            // Màu đỏ cho trạng thái "có xe/đã khóa" (Parking)
            analogWrite(pinParkingR, 0);    // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingG, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingB, 255); // CHỈNH SỬA ĐÂY
            Serial.println("Set LED to Red (Parking - Occupied)");
        } else if (strcmp(command, "reserve") == 0 || strcmp(command, "reserved") == 0) {
            // Màu xanh dương cho trạng thái "đặt trước" (Parking)
            analogWrite(pinParkingR, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingG, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingB, 0);    // CHỈNH SỬA ĐÂY
            Serial.println("Set LED to Blue (Parking - Reserved)");
        } else if (strcmp(command, "maintenance") == 0 || strcmp(command, "error") == 0) {
            // Màu vàng cho trạng thái "bảo trì/lỗi" (Parking)
            analogWrite(pinParkingR, 0);    // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingG, 0);    // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingB, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingR, 0); // Đảm bảo màu vàng (Red + Green) - CHỈNH SỬA ĐÂY - Thừa dòng này
            analogWrite(pinParkingG, 0); // CHỈNH SỬA ĐÂY - Thừa dòng này
            analogWrite(pinParkingB, 255); // CHỈNH SỬA ĐÂY - Thừa dòng này
            Serial.println("Set LED to Yellow (Parking - Maintenance/Error)");
        } else if (strcmp(command, "default") == 0 || strcmp(command, "unknown") == 0) {
            // Màu trắng/Tắt cho trạng thái "mặc định/không xác định" (Parking)
            analogWrite(pinParkingR, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingG, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingB, 255); // CHỈNH SỬA ĐÂY
            Serial.println("Set LED to White/Off (Parking - Default/Unknown)");
        } else {
            // Command không xác định (Parking)
            analogWrite(pinParkingR, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingG, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingB, 255); // CHỈNH SỬA ĐÂY
            Serial.println("Unknown command (Parking), LED Off");
        }
    }
}

void reconnect() {
    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        // Sử dụng Client ID duy nhất
        if (client.connect(("NodeMCU_MultiFunction_" + String(ESP.getChipId())).c_str())) { // Client ID chung
            Serial.println("Connected to MQTT broker");
            // Subscribe vào topic cho xe đạp và chỗ đỗ xe
            client.subscribe("bike/status/#");
            client.subscribe("parking/command"); // Subscribe topic đơn giản cho parking command

        } else {
            Serial.print("Failed to connect MQTT, rc=");
            Serial.println(client.state());
            delay(5000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    pinMode(pinR, OUTPUT);
    pinMode(pinG, OUTPUT);
    pinMode(pinB, OUTPUT);
    pinMode(speakerPin, OUTPUT);

    // CHỈNH SỬA ĐÂY: pinMode cho các chân RGB LED của chỗ đỗ xe
    pinMode(pinParkingR, OUTPUT);
    pinMode(pinParkingG, OUTPUT);
    pinMode(pinParkingB, OUTPUT);

    // Cấu hình chân nút nhấn là INPUT_PULLUP
    pinMode(buttonPin, INPUT_PULLUP);

    // Tắt LED ban đầu cho cả xe đạp và chỗ đỗ xe (tắt cả 2 bộ LED nếu có)
    analogWrite(pinR, 255);
    analogWrite(pinG, 255);
    analogWrite(pinB, 255);
    analogWrite(pinParkingR, 255);
    analogWrite(pinParkingG, 255);
    analogWrite(pinParkingB, 255);

    WiFi.begin(ssid, wifiPassword);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("WiFi connected");

    client.setServer(mqtt_server, 1883);
    client.setCallback(callback);
}

void loop() {
    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    // Đọc trạng thái nút nhấn (đã thêm debounce)
    int buttonState = digitalRead(buttonPin);
    if (buttonState == LOW) { // Nút nhấn được nhấn (INPUT_PULLUP nên LOW khi nhấn)
        unsigned long currentMillis = millis();
        if (currentMillis - lastButtonPress >= buttonDebounceDelay) {
            lastButtonPress = currentMillis;
            Serial.println("Button Pressed!");

            // Tạo JSON payload để gửi thông tin slot_number
            JsonDocument doc;
            doc["slot_number"] = localParkingSlotId;
            char jsonPayload[128];
            serializeJson(doc, jsonPayload);

            // Gửi thông tin qua MQTT topic (ví dụ: "parking/button_event")
            client.publish("parking/button_event", jsonPayload);
            Serial.print("Sent MQTT message: ");
            Serial.println(jsonPayload);
            analogWrite(pinParkingR, 0);    // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingG, 255); // CHỈNH SỬA ĐÂY
            analogWrite(pinParkingB, 255); // CHỈNH SỬA ĐÂY
            Serial.println("Set LED to Red (Parking - Occupied)");
        }
    }
}
