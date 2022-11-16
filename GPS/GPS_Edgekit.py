#!/usr/bin/env python3

# prequires: pip3 install pynmeagps

import os
import subprocess
import time
import Jetson.GPIO as GPIO

from pynmeagps import NMEAReader

GPIO.setwarnings(False)
GPIO.setmode(GPIO.CVM)

#define UARTMUX0 for communcation with GPS Module instead of E-Key
GPIO.setup("GPIO12", GPIO.OUT, initial=GPIO.HIGH)


with open("/dev/ttyTHS2", "rb") as f:
	_ = f.readline()  # remove the first line since it may be incomplete
	for _ in range(100):
		data = f.readline()
		msg = NMEAReader.parse(data)
		if msg == None: continue
		print(msg)