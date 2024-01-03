#include <LM335.h>

#include "Arduino.h"
class FAN {
public:
  FAN(int mPin);
  void setup();
  void highSpeed();
  void medSpeed();
  void lowSpeed();
  void off();
private:
  int _pin;
  int _low = 155;
  int _medium = 205;
  int _high = 255;
};

FAN::FAN(int mPin) {
  _pin = mPin;
}

void FAN::setup() {
  pinMode(_pin, OUTPUT);
}

void FAN::highSpeed() {
  analogWrite(_pin, _high);
}

void FAN::medSpeed() {
  analogWrite(_pin, _medium);
}

void FAN::lowSpeed() {
  analogWrite(_pin, _low);
}

void FAN::off() {
  analogWrite(_pin, 0);
}

// global variables
float tempC;
// initialise classses
LM335 tempSensor(5.04, 0);
FAN fan(5);

void setup() {
  Serial.begin(9600);
  fan.setup();
}

void loop() {
  // check the temp reading
  Serial.print("Celcius: ");
  tempC = tempSensor.measureC();
  Serial.println(tempC);

  // action the fan
  if (tempC < 50) {
    fan.highSpeed();
  } else {
    fan.off();
  }
  Serial.println("Fanspeed: HIGH");

  // wait a while
  delay(100);
}
