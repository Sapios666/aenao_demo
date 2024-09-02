import csv
import time
import board
import digitalio
import adafruit_lis3dh
import sys

seconds = 10 # 10 seconds
g_force = 9.8
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D6)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

filename = "data/vib_sample.csv" # Overwrite one file
#filename = "data/vib_sample_" + sys.argv[1] + ".csv" # Write different file

with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["x", "y", "z"])

with open(filename, 'a', newline='') as file:
	writer = csv.writer(file)
	for i in range(0,200*seconds):
		x, y, z = lis3dh.acceleration
		# print(x, y, z)
		writer.writerow([str(x/g_force), str(y/g_force), str(z/g_force)])
		time.sleep(0.005) # 1/sampling rate = 1/200Hz = 5msec 
