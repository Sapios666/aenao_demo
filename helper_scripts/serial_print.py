import time
import serial
import csv

ser = serial.Serial(port='/dev/ttyACM0',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

filename = "./samples.csv" # Overwrite one file

with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)

with open(filename, 'a', newline='') as file:
	writer = csv.writer(file)
	while True:
		data_read = ser.readline()
		data_read = data_read.strip()
		data_read = data_read.decode("utf-8")
		print(data_read)
		writer.writerow([str(data_read)])
		
