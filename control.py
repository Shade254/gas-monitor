#!/usr/bin/env python

from mqtt_connect import send_message
from air_module import air_sensor
from iwlistparse import scan_wifi

send_message(air_sensor + iwlistparse)
