import time
import serial
import csv

ser = serial.Serial(port='/dev/ttyACM0',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

while True:
	data_read = ser.readline()
	data_read = data_read.strip()
	print(data_read.decode("utf-8"))
	# time.sleep(0.2)