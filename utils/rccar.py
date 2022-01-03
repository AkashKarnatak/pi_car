#!/usr/bin/env python3

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
import argparse

# initialize
MOTOR_LEFT_1 = 11
MOTOR_LEFT_2 = 12
MOTOR_RIGHT_1 = 13
MOTOR_RIGHT_2 = 15

# setup
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(MOTOR_LEFT_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_LEFT_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_RIGHT_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_RIGHT_2, GPIO.OUT, initial=GPIO.LOW)

def forward():
    print('forward')
    GPIO.setup(MOTOR_LEFT_1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MOTOR_LEFT_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_RIGHT_1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MOTOR_RIGHT_2, GPIO.OUT, initial=GPIO.LOW)

def left():
    print('left')
    GPIO.setup(MOTOR_LEFT_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_LEFT_2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MOTOR_RIGHT_1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MOTOR_RIGHT_2, GPIO.OUT, initial=GPIO.LOW)

def right():
    print('right')
    GPIO.setup(MOTOR_LEFT_1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MOTOR_LEFT_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_RIGHT_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_RIGHT_2, GPIO.OUT, initial=GPIO.HIGH)

def back():
    print('back')
    GPIO.setup(MOTOR_LEFT_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_LEFT_2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MOTOR_RIGHT_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_RIGHT_2, GPIO.OUT, initial=GPIO.HIGH)

def stop():
    print('stop')
    GPIO.setup(MOTOR_LEFT_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_LEFT_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_RIGHT_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(MOTOR_RIGHT_2, GPIO.OUT, initial=GPIO.LOW)

parser = argparse.ArgumentParser(description='RPICAR go brrrrrrrrrrr')

parser.add_argument(
    'func', help='Function to execute')

args = parser.parse_args()

eval(f'{args.func}()')
