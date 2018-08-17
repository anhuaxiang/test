import numpy as np
import tensorflow as tf

# x1 = tf.constant([[3., 3.]])
# x2 = tf.constant([[2.], [2.]])
# out = tf.matmul(x1, x2)
#
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# result = sess.run(out)
# print(result)


with tf.Session() as sess:
    with tf.device("/cpu:0"):
        x1 = tf.constant([[3., 3.]])
        x2 = tf.constant([[2.], [2.]])
        out = tf.matmul(x1, x2)
        result = sess.run(out)
        print(result)
