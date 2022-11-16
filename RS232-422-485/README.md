### General
Es muss der GPIO13 oder innerhalb des Jetsons pin 38 auf high gezogen werden, um die UART Kommunikation vom 40 Pin Header (/dev/ttyTHS1) auf den internen zu legen


### Features

- Slew lmt macht die Flanken langsamer (EMV), Pin15 auf dem Port Expander. Wenn PIN15 High, dann ist enabled, dann 250kbit/s (betrifft alle MODI)
- Terminierung 120 Ohm am Empfänger, wenn der Termination Pin auf HIGH Ist wird terminiert (RS422/485)
- Funktioniert nur mit Flow Control 
