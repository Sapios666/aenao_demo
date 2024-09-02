import os
import csv
import subprocess
import time
from datetime import datetime

MAX = 65
filename = "data/temperature.csv" # Overwrite one file

with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["timestamp", "temperature"])

with open(filename, 'a', newline='') as file:
	writer = csv.writer(file)
	for i in range(0, 10):
		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		s = subprocess.getstatusoutput(f'vcgencmd measure_temp')
		text = s[1]
		temp = float(text[5:9])
		writer.writerow([timestamp, temp])
		print(temp)
		if(temp > MAX):
			os.system('shutdown now')
		time.sleep(60)