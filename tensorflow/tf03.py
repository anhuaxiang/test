import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import input_data


mnist = input_data.read_data_sets('data/', one_hot=True)
trainimg = mnist.train.images
trainlabel = mnist.train.labels
testimg = mnist.test.images
testlabel = mnist.test.labels
print('mnist loaded')
print(trainimg.shape)
print(trainlabel.shape)
print(testimg.shape)
print(testlabel.shape)
# [ 0.  0.  0.  0.  0.  0.  0.  1.  0.  0.]
print(trainlabel[0])

x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float', [None, 10])
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
actv = tf.nn.softmax(tf.matmul(x, w) + b)

cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(actv), reduction_indices=1))
learning_rate = 0.01
optm = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# tf.argmax(actv, 1)预测值取行的最大值的索引值，即预测结果
# tf.argmax(y, 1) 取实际值行的最大值的索引值，及标签结果
# 比较是否相等true or false
pred = tf.equal(tf.argmax(actv, 1), tf.argmax(y, 1))
# cast() 将True False 转化为float 0 or 1
accer = tf.reduce_mean(tf.cast(pred, "float"))

init = tf.global_variables_initializer()
training_epochs = 100
batch_size = 100
display_step = 5
sess = tf.Session()
sess.run(init)
for epoch in range(training_epochs):
    avg_cost = 0
    num_bach = int(mnist.train.num_examples/batch_size)
    for i in range(num_bach):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        sess.run(optm, feed_dict={x: batch_xs, y: batch_ys})
        feeds = {x: batch_xs, y: batch_ys}
        avg_cost += sess.run(cost, feed_dict=feeds)/num_bach

    if epoch % display_step == 0:
        feeds_train = {x: batch_xs, y: batch_ys}
        feeds_test = {x: mnist.test.images, y: mnist.test.labels}
        train_acc = sess.run(accer, feed_dict=feeds_train)
        test_acc = sess.run(accer, feed_dict=feeds_test)
        print("epoch:%03d/%03d  cost:%.9f  train_acc:%.3f  test_acc:%.3f" %
              (epoch, training_epochs, avg_cost, train_acc, test_acc))
print("done")
