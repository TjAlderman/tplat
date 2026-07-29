/*
  Fan.h - Library for control of 5V desk fan. Specified PWM mPin 
  is wired to base of transistor to enable control of fan speed.
*/
#include "Arduino.h"
#include "Fan.h"

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