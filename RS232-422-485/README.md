### General
GPIO13 or within the Jetson pin 38 must be pulled high to put the UART communication from the 40 pin header (/dev/ttyTHS0) to the internal one

### Before Installation
pip3 install gpio

### Features

- Slew lmt makes edges slower (EMC), pin15 on port expander. If PIN15 is high, then enabled, then 250kbit/s (affects all MODI).
- Termination 120 Ohm on receiver, if termination pin is HIGH it will terminate (RS422/485)
- Works only with Flow Control 
