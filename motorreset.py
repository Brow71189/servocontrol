import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

StepPins = [i for i in range(0,28)]

for pin in StepPins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)

