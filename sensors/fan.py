import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

while True:
    print ("test")
    GPIO.output(12, GPIO.HIGH)
    sleep(4)
    GPIO.output(12, GPIO.LOW)
    sleep(2)
