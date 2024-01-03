/*
  LM335.h - Library for control of LM335 temperature sensor.
*/
#ifndef LM335_H
#define LM335_H

#include "Arduino.h"

class LM335 {
  public:
    LM335(float mCal, int mPin); // to initialise an instance of the class, we must specify mCal and mPin
    // the class has the following methods
    float measureV(); 
    float measureK();
    float measureC();
    float measureF();
    float measureRankine();
  private:
    // the class has the following internal variables
    float _cal;
    int _pin;
};

#endif