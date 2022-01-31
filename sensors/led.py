"""Testing GPIO pins with 3 Leds (RGB) on Breadboard"""

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

red_led, blue_led, green_led = (23, 24, 25)

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led,GPIO.OUT)
GPIO.setup(green_led,GPIO.OUT)

while True:
    GPIO.output(red_led, GPIO.LOW)
