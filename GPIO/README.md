# General 

EdgeKit has 3 internal GPIO chips. 
1x Jetson own GPIO chip
1-2x Portexpander via i2c (1x on the Mainboard, 1x on the Industrial board (if choosen))  

Install `gpiod` to have an easy access to the gpio pins (`sudo apt install -y gpiod`).
With `gpioinfo` the GPIOs can be displayed. The output returns the list of the GPIO pins and the current status


## Get the gpio based on its name

With `gpiofind` you can get the chip and lane of a gpio pin:
```bash
$ gpiofind "GPIO_P0.6 - User Button"
gpiochip3 9
```


## Read the state of a gpio pin

With `gpioget` you can read the state of a pin (high/low):
```bash
$ gpioget gpiochip3 9
0
```


## Set state of a GPIO output

With `gpioset` you can set the state of a pin (high/low):
```bash
$ gpiofind "GPIO_P0.5"
gpiochip3 5
$ gpioget gpiochip3 5
0
$ gpioset gpiochip3 5=1
$ gpioget gpiochip3 5
1
$ gpioset gpiochip3 5=0
$ gpioget gpiochip3 5
0
```
