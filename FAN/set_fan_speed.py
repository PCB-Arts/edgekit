import sys

pwm_speed = 250

print('The fan speed will be set to %s'%(pwm_speed))

original_stdout = sys.stdout # Save a reference to the original standard output

with open('/sys/devices/pwm-fan/target_pwm', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('%s'%(pwm_speed))
    sys.stdout = original_stdout # Reset the standard output to its original value