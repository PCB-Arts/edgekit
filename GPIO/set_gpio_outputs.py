#!/usr/bin/env python3
"""
This is a demo script to set the output of gpio pins.
Make sure the package gpiod is installed (`apt install -y gpiod`).
"""

import os
import time


# choose the name of the GPIO PIN - use `gpioinfo` to get a list of gpio pins
GPIO_NAME = "GPIO_P0.1"


# get the lane the GPIO is connected to
gpio_lane = os.popen(f'gpiofind "{GPIO_NAME}"').read().strip()

for _ in range(5):
	# set the gpio_lane to high
	os.popen(f"gpioset {gpio_lane}=1").read().strip()
	print(f"{GPIO_NAME} set to high")
	time.sleep(1)
	# set the gpio_lane to low
	os.popen(f"gpioset {gpio_lane}=0").read().strip()
	print(f"{GPIO_NAME} set to low")
	time.sleep(1)
