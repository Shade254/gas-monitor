#!/usr/bin/env python
import time
import json
import datetime
import mqtt_connect
from air_module import air_sensor
from iwlistparse import scan_wifi
from Trilateration import trilat
from rgb_module import rgb_led

def get_routers_positions():
	return {"57.052359N,9.910457E":-44, "57.050374N,9.912322E":-45, "57.051868N,9.912837E":-54}

def on_message(client, userdata, message):
	if message.payload == "1":
		rgb_led(255, 0, 0)
	else if message.payload == "-1":
		rgb_led(0, 0, 255)
	else message.payload:
		rgb_led(0, 255, 0)

delay = 5


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

