#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GREEN_LED = 22
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.output(GREEN_LED, True)
time.sleep(10)
GPIO.output(GREEN_LED, False)

