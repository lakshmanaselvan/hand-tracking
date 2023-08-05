const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      Serial.println("ok");
      digitalWrite(ledPin, HIGH);
    } else if (command == '0') {
      Serial.println("no");
      digitalWrite(ledPin, LOW);
    }
  }
}

