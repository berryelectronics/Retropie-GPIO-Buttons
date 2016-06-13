import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.IN)	#UP
GPIO.setup(0, GPIO.IN)	#DOWN
GPIO.setup(5, GPIO.IN)	#LEFT
GPIO.setup(6, GPIO.IN)	#RIGHT
GPIO.setup(12, GPIO.IN)	#A
GPIO.setup(13, GPIO.IN)	#B
GPIO.setup(19, GPIO.IN)	#L
GPIO.setup(16, GPIO.IN)	#R
GPIO.setup(26, GPIO.IN)	#START
GPIO.setup(20, GPIO.IN)	#SELECT
GPIO.setup(21, GPIO.IN)	#KILL_ES

events = ([
	uinput.KEY_UP, 		#UP
	uinput.KEY_DOWN, 	#DOWN
	uinput.KEY_LEFT, 	#LEFT
	uinput.KEY_RIGHT,	#RIGHT
	uinput.KEY_A,		#A
	uinput.KEY_B,		#B
	uinput.KEY_C,		#X
	uinput.KEY_D,		#Y
	uinput.KEY_L,		#L
	uinput.KEY_R,		#R
	uinput.KEY_X,		#START
	uinput.KEY_Y,		#SELECT
	uinput.KEY_FN_F4	#KILL_ES
	])

device = uinput.Device(events)

pressedUp = False
pressedDown = False
pressedLeft = False
pressedRight = False
pressedA = False
pressedB = False
pressedL = False
pressedR = False
pressedStart = False
pressedSelect = False
pressedKillES = False

while True:
	if GPIO.input(1) and not pressedUp:
		device.emit(uinput.KEY_UP, 1)
		pressedUp = True
	elif not GPIO.input(1) and pressedUp:
		device.emit(uinput.KEY_UP, 0)
		pressedUp = False
		
	if GPIO.input(0) and not pressedDown:
		device.emit(uinput.KEY_DOWN, 1)
		pressedDown = True
	elif not GPIO.input(0) and pressedDown:
		device.emit(uinput.KEY_DOWN, 0)
		pressedDown = False	
	
	if GPIO.input(5) and not pressedLeft:
		device.emit(uinput.KEY_LEFT, 1)
		pressedLeft = True
	elif not GPIO.input(5) and pressedLeft:
		device.emit(uinput.KEY_LEFT, 0)
		pressedLeft = False	
	
	if GPIO.input(6) and not pressedRight:
		device.emit(uinput.KEY_RIGHT, 1)
		pressedRight = True
	elif not GPIO.input(6) and pressedRight:
		device.emit(uinput.KEY_RIGHT, 0)
		pressedRight = False	
		
	if GPIO.input(12) and not pressedA:
		device.emit(uinput.KEY_A, 1)
		pressedA = True
	elif not GPIO.input(12) and pressedA:
		device.emit(uinput.KEY_A, 0)
		pressedA = False	
		
	if GPIO.input(13) and not pressedB:
		device.emit(uinput.KEY_B, 1)
		pressedB = True
	elif not GPIO.input(13) and pressedB:
		device.emit(uinput.KEY_B, 0)
		pressedB = False	
		
	if GPIO.input(19) and not pressedL:
		device.emit(uinput.KEY_L, 1)
		pressedL = True
	elif not GPIO.input(19) and pressedL:
		device.emit(uinput.KEY_L, 0)
		pressedL = False	
		
	if GPIO.input(16) and not pressedR:
		device.emit(uinput.KEY_R, 1)
		pressedR = True
	elif not GPIO.input(16) and pressedR:
		device.emit(uinput.KEY_R, 0)
		pressedR = False	
		
	if GPIO.input(26) and not pressedStart:
		device.emit(uinput.KEY_X, 1)
		pressedStart = True
	elif not GPIO.input(26) and pressedStart:
		device.emit(uinput.KEY_X, 0)
		pressedStart = False	
		
	if GPIO.input(20) and not pressedSelect:
		device.emit(uinput.KEY_Y, 1)
		pressedSelect = True
	elif not GPIO.input(20) and pressedSelect:
		device.emit(uinput.KEY_Y, 0)
		pressedSelect = False	
		
	if GPIO.input(21) and not pressedKillES:
		device.emit(uinput.KEY_FN_F4, 1)
		pressedKillES = True
	elif not GPIO.input(21) and pressedKillES:
		device.emit(uinput.KEY_FN_F4, 0)
		pressedKillES = False	
	
	time.sleep(0.01)

