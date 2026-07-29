/*
  LM335.h - Library for control of LM335 temperature sensor.
*/
#include "Arduino.h"
#include "LM335.h"

LM335::LM335(float mCal, int mPin)
{
  _cal = mCal; // supply voltage (used for calibration)
  _pin = mPin; // analog pin
}
// methods
float LM335::measureV()
{
  float retVal = (float) analogRead(_pin);
  retVal = (retVal*_cal)/1024.0;
  return retVal;
}
float LM335::measureK()
{
  return measureV()/0.01;//10mV/k
}
float LM335::measureC()
{
  return (measureV()/0.01)-273.15;
}
float LM335::measureF()
{
  return (((measureV()/0.01)-273.15)*1.8)+32;
}