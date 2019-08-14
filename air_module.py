import time
import Adafruit_DHT

def air_sensor():
 DHT_SENSOR = Adafruit_DHT.DHT22
 DHT_PIN = 21
 humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
 data_table = {}
 (data_table["humidity"],data_table["temperature"]) = (humidity, temperature)
 return data_table

#print(air_sensor())