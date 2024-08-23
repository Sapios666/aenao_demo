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

def send_weight(weight):		
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	# Post to endpoint
	payload = json.dumps({
		"binID": "1",
		"userID": "564994897833",
		'timestamp': str(timestamp),
		"weight": str(weight),
		"metric_weight": "kg"
	})
	
	'''
		payload = json.dumps({
			"binID": "1",
			"userID": "564994897833",
			'timestamp': str(timestamp),
			"weight": str(weight),
			"metric_weight": "kg",
			"total_weight": "3555",
			"total_count": "6",
			"fill_level": "16",
			"fill_metric":"%"
		})
	'''
	
	# Post to endpoint
	response = requests.request("POST", url_user, headers=headers, data=payload)
	print(response.json())