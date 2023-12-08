#!/usr/bin/env python3

import os
import time


def export(gpio):
	""" Export a gpio port to sysfs for usage """
	if not os.path.exists(f"/sys/class/gpio/gpio{gpio}"):
		with open("/sys/class/gpio/export", "w") as f:
			f.write(gpio)


def unexport(gpio):
	""" Unexport a gpio port after usage """
	if os.path.exists(f"/sys/class/gpio/gpio{gpio}"):
		with open("/sys/class/gpio/unexport", "w") as f:
			f.write(gpio)


def set_output(gpio):
	""" Define a gpio port as output """
	with open(f"/sys/class/gpio/gpio{gpio}/direction", "w") as f:
		f.write("out")


def set_input(gpio):
	""" Define a gpio port as input """
	with open(f"/sys/class/gpio/gpio{gpio}/direction", "w") as f:
		f.write("in")


def read_value(gpio):
	""" Read the value of a gpio input """
	with open(f"/sys/class/gpio/gpio{gpio}/value") as f:
		return f.read()


def set_high(gpio):
	""" Set the output of a gpio to high (1) """
	with open(f"/sys/class/gpio/gpio{gpio}/value", "w") as f:
		f.write("1")


def set_low(gpio):
	""" Set the output of a gpio to low (0) """
	with open(f"/sys/class/gpio/gpio{gpio}/value", "w") as f:
		f.write("0")
