import numpy as np
import tensorflow as tf


x_data = np.float32(np.random.rand(2, 100))
# print(x_data)
y_data = np.dot([1.100, 0.200], x_data) + 0.300
# print(y_data)

b = tf.Variable(tf.zeros([1]))
w = tf.Variable(tf.random_normal([1, 2], -1.0, 1.0))
y = tf.matmul(w, x_data) + b

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(w), sess.run(b), float(sess.run(loss)))