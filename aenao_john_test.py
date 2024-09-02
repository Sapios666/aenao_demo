#!/usr/bin/env python

import time
import subprocess
import multiprocessing
import sys

from datetime import datetime

import requests
import json

url_motor = "http://160.40.49.238:8000/api/bins"
url_user = "http://160.40.49.238:8000/api/userBin"

headers = {
  'Content-Type': 'application/json'
}

motor_sleep = 15*60
general_sleep = 30*60

def normal_mode():
	while(1):
		print("Normal mode")
		
		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	        # Post to endpoint
		payload = json.dumps({
			"binID": "1",
			"userID": "564994897833",
			'timestamp': str(timestamp),
			"weight": "3",
			"metric_weight": "g",
			"total_weight": "3555",
			"total_count": "6",
			"fill_level": "16",
			"fill_metric":"%"
		})

		# Post to endpoint
		response = requests.request("POST", url_user, headers=headers, data=payload)
		print(response.json())

		# Sleep for 5 sec
		time.sleep(general_sleep)
    
def validation_mode():
	while(1):
		print("Motor Validation")

		# Motor data
		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		payload = json.dumps({
			'binID': 1,
			'timestamp': timestamp,
			'metrics': [
			{
				'type': 'Audio',
				'status': 'OK'
			},
			{
				'type': 'Vibrations',
				'status': 'OK',
				'x': 0.1,
				'y': 0.2,
				'z': 13.2,
				'metric': '%'
			},
			{
				'type': 'Power',
				'value': 1.2,
				'metric': 'kW'
			}],
			"total_weight": "55",
			"total_count": "6",
			"fill_level": "16",
			"fill_metric":"%"
		})

		# Post to endpoint
		response = requests.request("POST", url_motor, headers=headers, data=payload)
		print(response.json())

		# Sleep for 5 sec
		time.sleep(motor_sleep)

def main():
	# creating processes
	p1 = multiprocessing.Process(target=normal_mode)
	p2 = multiprocessing.Process(target=validation_mode)
	# starting process 1
	p1.start()
	# starting process 2
	p2.start()
	# wait until process 1 is finished
	p1.join()
	# wait until process 2 is finished
	p2.join()

if __name__ == "__main__":
	try:
		# main()
		# normal_mode()
		validation_mode()
	finally:
		print("--------------")
		print("GPIO.cleanup()")
		print("--------------")
		GPIO.cleanup()

	sys.exit()


