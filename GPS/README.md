### General 

This test script shows the communication with the GPS module (u-blox m8n) and prints the raw data on the CLI. 

### Usage

`python3 GPS_Edgekit.py `

### UART /dev/ttyTHS2 MUX 

First the GPIO 12 (pin 194 in the Jetson must be pulled high), 
this ensures that the MUX from the E-Key points to the GPS module.

### Before sending commands to the GPS module

When communicating via /dev/ttyTHS2, error messages are sent from the GPS receiver, since Linux automatically sends responses back on this interface. These responses can be switched off with the command `stty -F /dev/ttyTHS2 -echo`.

### References

Documentation for the GPS format: 
- https://navspark.mybigcommerce.com/content/NMEA_Format_v0.1.pdf

Library:
- https://pypi.org/project/pyubx2/

U-Blox Module: 
- https://www.u-blox.com/sites/default/files/NEO-M8-FW3_DataSheet_UBX-15031086.pdf
