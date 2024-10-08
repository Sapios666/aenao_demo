import RPi.GPIO as GPIO
import time
import sys
import signal
import serial

GPIO.setmode(GPIO.BOARD)

DOOR_SENSOR_PIN = 12

isOpen = None
oldIsOpen = None
valueOpen = 0
valueClosed = 0

GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def readValue():
	# measurement value
	value = 0
	#Open a serial port that is connected to an Arduino
	ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)
	ser.flushInput()

	for i in range(5):
		# Read in data from Serial until \n (new line) received
		ser_bytes = ser.readline()

	for i in range(5):
		# Read in data from Serial until \n (new line) received
		ser_bytes = ser.readline()
		# Convert received bytes to text format
		decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode())
		# print(decoded_bytes)
		value += int(decoded_bytes)

	# Close serial port
	ser.close()
	# Average measurements
	value = value//5
	# Write received data to variable
	return value

while True:
	oldIsOpen = isOpen
	isOpen = GPIO.input(DOOR_SENSOR_PIN)

	if (isOpen and (isOpen != oldIsOpen)):
		print("Door Open")
		#valueOpen = readValue()
		#print(valueOpen)
	elif (isOpen != oldIsOpen):
		print("Door Closed")
		#valueClosed = readValue()
		#print(valueClosed)
		#print("Difference = " + str(valueClosed-valueOpen))

	time.sleep(1)