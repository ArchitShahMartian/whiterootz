import RPi.GPIO as GPIO
import argparse
from time import sleep

fan_pin = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fan_pin, GPIO.OUT)

parser = argparse.ArgumentParser(description='Enter 1 to turn off and 0 to turn on led')
parser.add_argument('-i', dest='integer', choices=['1', '0'], help='Enter 1 or 0')
args = parser.parse_args()

GPIO.output(fan_pin, int(args.integer[0]))


# def device_turn_off_on(pin, state):
#     print ("device_turn_off_on", pin, state)
#     GPIO.output(pin, state)

# while True:
#     GPIO.output(12, GPIO.HIGH)
#     sleep(2)
#     GPIO.output(12, GPIO.LOW)
#     sleep(10)
