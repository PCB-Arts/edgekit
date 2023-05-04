## General 
If you have an installed FAN on EdgeKit, it's possible to manually set the speed or read the RPM. This just works with Ubuntu 18.04. You could check which ubuntu is running by running the command "lsb_release -a". 

### Ubuntu 18.04
### Set PWM Speed 
echo 127 > /sys/devices/pwm-fan/target_pwm

Where 127 could be a value from 0 - 255. 0 = fan not moving; 255 = fan moving with max speed.

### Read the actual RPM

Enable the tacho first:
echo 1 > /sys/devices/pwm-fan/tach_enable

Then you can read the actual speed with:
cat /sys/devices/pwm-fan/rpm_measured

### Ubuntu 20.04
nvfancontrol is a userspace fan speed control daemon. This manages Fan speed based on Temperature to Fan speed mapping table in nvfancontrol configuration file (/etc/nvfancontrol.conf). 

Check actual profile: sudo nvfancontrol -q
