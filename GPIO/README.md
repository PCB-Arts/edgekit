### General 

EdgeKit has 3 internal GPIO chips. 
1x Jetson own GPIO chip
2x Portexpander via i2c

With `cat /sys/kernel/debug/gpio` the GPIOs can be displayed. The output returns the number of the GPIO pins and the current status

### Configure GPIO as input or output: 

To configure a GPIO you have to create it first. Then you have to decide the direction. So either as input or output. First we switch on the GPIO 487.

`echo 487 > /sys/class/gpio/export`
If the GPIO should be configured as input, then the following command applies.

`echo in > /sys/class/gpio/gpio487/direction`
If the GPIO should be configured as output, then the following command is valid.

`echo out > /sys/class/gpio/gpio487/direction`
A GPIO configured as output should be given a state, i.e. "high" or "low".

### Set state of a GPIO output
Basically you can only set outputs. To set the state of a GPIO output to "high" the following command is sufficient.

`echo 1 > /sys/class/gpio/gpio487/value`
To set the state of a GPIO output to "low" the following command is sufficient.

`echo 0 > /sys/class/gpio/gpio487/value`

### Get GPIO state
To determine the state, i.e. "high" or "low", at a GPIO, the following command is sufficient. The GPIO can be an input as well as an output.

`cat /sys/class/gpio/gpio487/value`
The output is "1" for "high" or "0" for "low".

### Disable GPIO
If you don't need GPIOs anymore, you should disable them. By the following commands the files and directories of the GPIOs disappear again. At a reboot the GPIOs will be reset automatically.

`echo gpio487 > /sys/class/gpio/unexport`