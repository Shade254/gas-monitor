#!/usr/bin/env python


import paho.mqtt.client as mqttClient
import time


def on_connect(client, userdata, flags, rc):

    if rc == 0:
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")



def init():
    global Connected
    Connected = False
    broker_address = "farmer.cloudmqtt.com"
    port = 18260
    user = "okvktwqa"
    password = "iMVcWeUY7yqa"
    
    global Client
    Client = mqttClient.Client("RaspberryPi")               #create new instance
    Client.username_pw_set(user, password=password)    #set username and password 
    Client.on_connect= on_connect                      #attach function to callback
    Client.connect(broker_address, port=port)          #connect to broker
    Client.loop_start()        #start the loop

    

def send_message(msg):
    global Connected
    Connected = False

    while Connected != True:
        init()
        time.sleep(0.1)

    global Client
    Client.publish("data", msg)
    Client.disconnect()
    Client.loop_stop()
