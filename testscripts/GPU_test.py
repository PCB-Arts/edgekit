# 
# Owner: PCB Arts GmbH
# Date: 2024-01-18
# Test script for GPU usage on the EdgeKit 
# Inspired by: https://www.tensorflow.org/guide/gpu?hl=en
# 

import tensorflow as tf 
import time
#Enable device placement logging
tf.debugging.set_log_device_placement(True)

# List available GPUs, one is available for our case
print(tf.config.list_physical_devices('GPU'))
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

time.sleep(4)
# Place tensors on the GPU
with tf.device('/GPU:0'):
    a = tf.constant([[1000.0, 2000.0, 3000.0], [4000.0, 5000.0, 6000.0]])
    b = tf.constant([[1000.0, 2000.0], [3000.0, 4000.0], [5000.0, 6000.0]])
    c = tf.matmul(a, b)
    print(c)


# Output: 
#   Num GPUs Available:  1
#   a: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
#   b: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
#   MatMul: (MatMul): /job:localhost/replica:0/task:0/device:GPU:0
#   product_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
#   tf.Tensor(
#   [[22. 28.]
#    [49. 64.]], shape=(2, 2), dtype=float32)
