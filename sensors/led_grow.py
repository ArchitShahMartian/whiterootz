import RPi.GPIO as GPIO
import argparse
from time import sleep

led_pin = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

parser = argparse.ArgumentParser(description='Enter 1 to turn off and 0 to turn on led')
parser.add_argument('-i', dest='integer', choices=['1', '0'], help='Enter 1 or 0')
args = parser.parse_args()

GPIO.output(led_pin, int(args.integer[0]))
