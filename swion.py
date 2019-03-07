#!/usr/bin/env python
    
from time import sleep

import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
	if ( GPIO.input(23) == False ):
		print ('encendido')
	sleep(0.1);
