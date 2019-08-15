#!/usr/bin/env python

import json
import datetime
from mqtt_connect import send_message
from air_module import air_sensor
from iwlistparse import scan_wifi

dict = air_sensor()
dict['stations'] = scan_wifi()
dict['datetime'] = datetime.datetime.now()

send_message(json.dump(dict))
