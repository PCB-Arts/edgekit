#!/usr/bin/env python3
"""
This is a demo script to read the input of gpio pins.
Make sure the package gpiod is installed (`apt install -y gpiod`).
"""

import os
import time


# choose the name of the GPIO PIN - use `gpioinfo` to get a list of gpio pins
GPIO_NAME = "GPIO_P0.6 - User Button"


# get the lane the GPIO is connected to
gpio_lane = os.popen(f'gpiofind "{GPIO_NAME}"').read().strip()

for _ in range(10):
	# read the gpio_lane value
	value = int(os.popen(f"gpioget {gpio_lane}").read().strip())
	print(value)
	time.sleep(1)
