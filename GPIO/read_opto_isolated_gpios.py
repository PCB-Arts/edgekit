#!/usr/bin/env python3
"""
This is a demo script to read the input of gpio pins.
Make sure the package gpiod is installed (`apt install -y gpiod`).
"""

import os
import time


# choose the name of the GPIO PIN - use `gpioinfo` to get a list of gpio pins
DI00 = "DI0.0"
DI01 = "DI0.1"
DI02 = "DI0.2"
DI03 = "DI0.3"
DI04 = "DI0.4"
DI05 = "DI0.5"
DI06 = "DI0.6"
DI07 = "DI0.7" 
DI10 = "DI1.0" 
DI11 = "DI1.1"
DI12 = "DI1.2" 
DI13 = "DI1.3" 

# get the lane the GPIO is connected to
gpio_lane = os.popen(f'gpiofind "{DI00}"').read().strip()

while 1:
	# read the gpio_lane value
	value = int(os.popen(f"gpioget {gpio_lane}").read().strip())
	print(value)
	# outcomment this time.sleep to have fast triggering options
	time.sleep(1)
	if (value == 0): 
		print ("trigger detected") 
