#!/usr/bin/env python
import time
import json
import datetime
from mqtt_connect import send_message
from air_module import air_sensor
from iwlistparse import scan_wifi
from Trilateration import trilat

def get_routers_positions():
	return {"57.052359N,9.910457E":-44, "57.050374N,9.912322E":-45, "57.051868N,9.912837E":-54}

delay = 10

print(get_routers_positions())

while True:
	dict = air_sensor()
	dict['stations'] = scan_wifi()
	dict['datetime'] = unicode(datetime.datetime.now())
	dict['coords'] = trilat(get_routers_positions())

	send_message(json.dumps(dict))
	print("Message sent ... ")
	time.sleep(10)

