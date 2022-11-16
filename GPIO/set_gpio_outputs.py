#!/usr/bin/env python3

from gpio import *


MODULE = "Nano"
# MODULE = "NX"

if MODULE == "Nano":
	DO00 = "487"  # Relais 1
	DO01 = "486"  # Relais 2
	DO10 = "485"
	DO11 = "484"
	DO12 = "483"
	DO13 = "481"
elif MODULE == "NX":
	DO00 = "223"  # Relais 1
	DO01 = "224"  # Relais 2
	DO10 = "221"
	DO11 = "220"
	DO12 = "219"
	DO13 = "217"
else:
	raise NotImplementedError("Unknown Module: %s", MODULE)


try:
	export(DO00)
	set_output(DO00)
	for _ in range(3):
		set_high(DO00)
		time.sleep(1)
		set_low(DO00)
		time.sleep(1)
except:
	pass
unexport(DO00)