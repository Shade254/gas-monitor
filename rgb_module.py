import RPi.GPIO as GPIO
def rgb_led(R,G,B):
 GPIO.setmode(GPIO.BCM)
 RED_PIN = 26
 GREEN_PIN = 19
 BLUE_PIN = 13
 GPIO.setup(RED_PIN,GPIO.OUT)
 GPIO.output(RED_PIN,0)
 GPIO.setup(GREEN_PIN,GPIO.OUT)
 GPIO.output(GREEN_PIN,0)
 GPIO.setup(BLUE_PIN,GPIO.OUT)
 GPIO.output(BLUE_PIN,0)
 GPIO.output(RED_PIN,R)
 GPIO.output(GREEN_PIN,G)
 GPIO.output(BLUE_PIN,B)

#rgb_led(34,0,77)