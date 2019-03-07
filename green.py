#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(GREEN_LED, True)
GPIO.output(RED_LED, False)
time.sleep(10)
GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, True)
time.sleep(10)
GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, False)

