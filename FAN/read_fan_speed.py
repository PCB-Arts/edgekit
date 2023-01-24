import sys

original_stdout = sys.stdout # Save a reference to the original standard output

#Enable Tacho 
with open('/sys/devices/pwm-fan/tach_enable', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('1')
    sys.stdout = original_stdout # Reset the standard output to its original value

#Read Tacho 
with open('/sys/devices/pwm-fan/rpm_measured', 'r') as f:
    tach_speed = f.read()

print('The fan speed is %s'%(tach_speed))