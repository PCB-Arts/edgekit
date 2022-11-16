#!/usr/bin/env python3

from gpio import *


MODULE = "Nano"
# MODULE = "NX"

if MODULE == "Nano":
	DI10 = "488"
	DI11 = "489"
	DI12 = "490"
	DI13 = "491"
	USER_BUTTON = "505"
elif MODULE == "NX":
	DI10 = "224"
	DI11 = "225"
	DI12 = "226"
	DI13 = "227"
	USER_BUTTON = "241"
else:
	raise NotImplementedError("Unknown Module: %s", MODULE)


try:
	export(USER_BUTTON)
	set_input(USER_BUTTON)
	for _ in range(3):
		print(read_value(USER_BUTTON), end="")
		time.sleep(1)
except:
	pass
unexport(USER_BUTTON)
