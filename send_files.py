import requests
import json
from pandas import *
from datetime import datetime
import os

def vib_request():
	try:
		url = "http://160.40.49.238:8000/api/maintenance"

		# Decide the two file paths according to your computer system
		csvFilePath = r'data/vib_sample.csv'

		# reading CSV file
		data = read_csv(csvFilePath)

		# converting column data to list
		x = data['x'].tolist()
		y = data['y'].tolist()
		z = data['z'].tolist()

		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		payload = json.dumps({
		  "binID": "1",
		  "timestamp": timestamp,
		  "x": x,
		  "y": y,
		  "z": z
		})

		headers = {
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		#print(response.text)
	except:
		print("Failed to connect with the endpoint")

def audio_request():
	try:
		url = "http://160.40.49.238:8000/api/audio-file"

		# Decide the two file paths according to your computer system
		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		new_filename = "data/audio/audio_" + timestamp + ".wav" # Write different file
		old_filename = 'data/audio/audio_sample.wav'
		command = "mv '" + old_filename + "' '" + new_filename + "'"
		os.system(command)

		payload = {}
		files=[
		  ('audio', (new_filename, open(new_filename, 'rb'), 'audio/wav'))
		]

		response = requests.request("POST", url, data=payload, files=files)

		#print(response.text)
		command = "rm '" + new_filename + "'"
		os.system(command)
	except:
		print("Failed to connect with the endpoint")

def amp_request():
	try:
		url = "http://160.40.49.238:8000/api/maintenance"

		# Decide the two file paths according to your computer system
		csvFilePath = r'data/vib_sample.csv'

		# reading CSV file
		data = read_csv(csvFilePath)

		# converting column data to list
		x = data['x'].tolist()
		y = data['y'].tolist()
		z = data['z'].tolist()

		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		payload = json.dumps({
		  "binID": "1",
		  "timestamp": timestamp,
		  "x": x,
		  "y": y,
		  "z": z
		})

		headers = {
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		#print(response.text)
	except:
		print("Failed to connect with the endpoint")
