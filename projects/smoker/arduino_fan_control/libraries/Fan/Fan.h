/*
  Fan.h - Library for control of 5V desk fan. Specified PWM mPin 
  is wired to base of transistor to enable control of fan speed.
*/
#ifndef FAN_H
#define FAN_H

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

#endif