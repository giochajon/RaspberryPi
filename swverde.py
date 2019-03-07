#!/usr/bin/env python
    
import time

import RPi.GPIO as GPIO
GREEN_LED = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
	if ( GPIO.input(23) == False ):
		GPIO.setup(GREEN_LED, GPIO.OUT)
		GPIO.output(GREEN_LED, True)
		time.sleep(5)
		GPIO.output(GREEN_LED, False)
	time.sleep(0.2);
