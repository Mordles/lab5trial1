#!/usr/bin/env python3

import PCF8591 as ADC

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 1)

def setup():
  ADC.setup(0x48)

def loop():
  while True:
    print(ADC.read(0))
    ADC.write(ADC.read(0))

def destroy():
  ADC.write(0)

setup()
while True:
  if (ADC.read(0) < 210):
    print(ADC.read(0))
    ADC.write(ADC.read(0))
  elif (ADC.read(0) > 210):
    GPIO.output(26, 0) 

"""
if __name__ == "__main__":
  try:
    setup()
    loop()
  except KeyboardInterrupt:
   destroy()
"""

