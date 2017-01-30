#Approximately 4254 steps for complete rotation


import sys
import time
#import pygame
import curses
from curses import wrapper
import os
import RPi.GPIO as GPIO

os.environ["SDL_VIDEODRIVER"] = "dummy"
#pygame.init()

stdscr = curses.initscr()
stdscr.keypad(True)
stdscr.nodelay(1)
curses.nocbreak()
curses.noecho()

def main(stdscr):

	Motor1 = [17,18,27,22]
	Motor2 = [23,24,25,4]
	
	GPIO.setmode(GPIO.BCM)
	for pin in Motor1:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
	
	
	for pin in Motor2:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
	
	Seq = [[0,0,0,1],
		[0,0,1,1],
		[0,0,1,0],
		[0,1,1,0],
		[0,1,0,0],
		[1,1,0,0],
		[1,0,0,0],
		[1,0,0,1]]
	
	StepCount = len(Seq)
	#Initialize Motor and direction
	m=1
	StepDir = 1
	stop=-1	# if stop = 1 stops the motor but not the program. If e is pressed, the program is closed
	
	if len(sys.argv) > 1:
		WaitTime = int(sys.argv[1])/float(1000)
	else:
		WaitTime = 10.0/float(1000)
	
	StepCounter = 0
	totalcount = 0	#Steps for complete rotation
	
	
 	c = stdscr.getch() # Initialization of c	
	while c!= ord('e'):
		
		#Use Keyboard as control
		c = stdscr.getch()		
		if c == curses.KEY_LEFT:
			m = 1
			StepDir = 1
			stop = -1
		if c == curses.KEY_RIGHT:
			m = 1
			StepDir = -1
			stop = -1
		if c == curses.KEY_UP:
			m = 2
			StepDir = 1
			stop = -1
		if c == curses.KEY_DOWN:
			m = 2
			StepDir = -1
			stop = -1
		if c == ord('f'):
			WaitTime = WaitTime / 2.0
		if c == ord('s'):
			WaitTime = WaitTime * 2.0
		if c == ord(' '):
			stop *= -1
		#print StepCounter
		#print Seq[StepCounter]
		for pin in range(0,4):
			if m == 1:
				xpin=Motor1[pin]
			if m == 2:
				xpin=Motor2[pin]
			if Seq[StepCounter][pin]!=0 and stop==-1:
				#print "Enable GPIO %i" %(xpin)
				GPIO.output(xpin, True)
			else:
				GPIO.output(xpin, False)
		StepCounter += StepDir
		totalcount += StepDir
	
		if (StepCounter>=StepCount):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = StepCount+StepDir
		time.sleep(WaitTime)
	#print "%i, "%(totalcount)
	time.sleep(3)

def resetmotor():
	for pin in range(0,28):
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
	
	return


wrapper(main)
resetmotor()

