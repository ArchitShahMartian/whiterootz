import RPi.GPIO as GPIO
import argparse
from time import sleep

humidifier_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(humidifier_pin, GPIO.OUT)

parser = argparse.ArgumentParser(description='Enter 1 to turn off and 0 to turn on led')
parser.add_argument('-i', dest='integer', choices=['1', '0'], help='Enter 1 or 0')
args = parser.parse_args()

GPIO.output(humidifier_pin, int(args.integer[0]))

