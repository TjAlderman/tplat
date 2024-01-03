#include <LM335.h>
#include <Fan.h>

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

  // action the fan based on the temp reading
  if (tempC < 50) {
    fan.highSpeed();
  } else {
    fan.off();
  }
  Serial.println("Fanspeed: HIGH");

  // wait a while
  delay(100);
}
