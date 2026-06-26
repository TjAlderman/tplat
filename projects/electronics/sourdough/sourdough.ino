#include <lm335.h>

// global variables
float tempC;
// initialise classses
LM335 tempSensor(5.04, 0);

void setup() {
  Serial.begin(9600);
}

void loop() {
  // check the temp reading
  Serial.print("Celcius: ");
  tempC = tempSensor.measureC();
  Serial.println(tempC);

  // wait a while
  delay(100);
}