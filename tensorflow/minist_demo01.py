import tensorflow as tf
import input_data

# 加载数据
mnist = input_data.read_data_sets('data/', one_hot=True)
y_train = tf.placeholder("float", [None, 10])
x = tf.placeholder("float", [None, 784])
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, w) + b)
cost = -tf.reduce_sum(y_train * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_train, 1))
accur = tf.reduce_mean(tf.cast(correct_prediction, "float"))
with tf.Session() as sess:
    init = tf.initialize_all_variables()
    sess.run(init)
    for i in range(1001):
        batch_x, batch_y = mnist.train.next_batch(100)
        t, c = sess.run([train_step, cost], feed_dict={x: batch_x, y_train: batch_y})
        print(i, c)
        if i % 10 == 0:
            print("准确率***********************************", sess.run(accur, feed_dict={x: mnist.test.images, y_train: mnist.test.labels}))
