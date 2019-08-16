#!/usr/bin/env python
import time
import json
import datetime
import mqtt_connect
from air_module import air_sensor
from iwlistparse import scan_wifi
from Trilateration import trilat
from rgb_module import rgb_led
import random

def get_random_coords():
	lat = random.uniform(56.901578, 57.290873)
	lon = random.uniform(9.576935, 10.302654)
	return [lat, lon]


def get_routers_positions():
	routers = {}
	for i in range(3):
		coords = get_random_coords();
		stri = str(coords[0]) + "N," + str(coords[1]) + "E"
		strength = -random.randrange(14, 60, 1)
		routers[stri] = strength
	return routers

def on_message(client, userdata, message):
	if message.payload == "1":
		rgb_led(255, 0, 0)
	elif message.payload == "-1":
		rgb_led(0, 0, 255)
	else:
		rgb_led(0, 255, 0)

delay = 5

print(get_routers_positions())
print(get_routers_positions())
print(get_routers_positions())
print(get_routers_positions())
print(get_routers_positions())
print(get_routers_positions())

mqtt_connect.init(on_message)
print("Starting connection")
time.sleep(1)

try:
	while True:
		dict = air_sensor()
		dict['stations'] = scan_wifi()
		dict['datetime'] = unicode(datetime.datetime.now())
		dict['coords'] = trilat(get_routers_positions())

		mqtt_connect.send_message(json.dumps(dict))
		print("Message sent")
		time.sleep(10)
except KeyboardInterrupt:
	print("Closing connections...")
	mqtt_connect.disconnect()

