### CAN Communication with EdgeKit

The EdgeKit with Xavier SOMs are capable of doing CAN communication. The instructions for setting up the CAN are from following medium article: 
https://medium.com/@ramin.nabati/enabling-can-on-nvidia-jetson-xavier-developer-kit-aaaa3c4d99c9

### CAN Setup

First of all we need to manually setup the CAN controller with the script "enable_CAN.sh". 
If you want the configuration fixed on boot just run following command in your shell: 

```
printf '%s\n' '#!/bin/bash' 'exit 0' | sudo tee -a /etc/rc.local
sudo chmod +x /etc/rc.local
``` 

And then open the rc.local file and add following line between #!/bin/bash and exit0:

```sh /usr/local/share/edgekit-samples/CAN/enable_CAN.sh &```

### Sending & Receiving CAN messages

Send single message with custom data:
```cansend can0 123#abcdabcd```

Send multiple messages with random data: 
```cangen -v can0```

Read all messages: 
```candump can0```

### Setting CAN 

Shutdown the CAN Interface first: 
```sudo ifconfig can0 down````

Set the bitrate of the CAN Interface first:
```sudo ip link set can0 up type can bitrate 1000000```

### CAN Termination

There is a build in CAN Termination, which is able to switch on with triggering a GPIO. To identify the GPIO Pin on your EdgeKit please type the following command (as sudo): 
```cat /sys/kernel/debug/gpio | grep CAN```
As an output you get an GPIO Pin, this pin you need to declare as an output and define the state. Low = Termination inactive, High = Termination active. 
```
echo X > /sys/class/gpio/export
echo out > /sys/class/gpio/gpioX/direction
\#For deactivating Termination
echo 0 > /sys/class/gpio/gpioX/value 
\#For activating Termination
echo 1 > /sys/class/gpio/gpioX/value 
```
