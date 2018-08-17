# coding:utf-8
import tensorflow as tf
import input_data

mnist = input_data.read_data_sets('data/', one_hot=True)

# 两层神经网络，初始化
# 有784个输入
# 第一层，w1[784*256]，b1 = 256
# 第二层，w2[256*128], b2 = 128
# 输出层，out[128*10], 有10个输出
n_hidden_1 = 256
n_hidden_2 = 128
n_input = 784
n_classes = 10

# x,y初始化
x = tf.placeholder('float', [None, n_input])
y = tf.placeholder('float', [None, n_classes])

# 参数初始化
stddev = 0.1
# 权重参数
weight = {
    'w1': tf.Variable(tf.random_normal([n_input, n_hidden_1], stddev=stddev)),
    'w2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2], stddev=stddev)),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes], stddev=stddev)),
}
# 偏置参数
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes])),
}


# 正向传播函数
def multilayer_perceptron(_x, _weight, _biases):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(_x, _weight['w1']), _biases['b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, _weight['w2']), _biases['b2']))
    return tf.matmul(layer_2, _weight['out']) + _biases['out']

pred = multilayer_perceptron(x, weight, biases)

# 损失值和损失函数
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=pred))
# cost = tf.reduce_mean(tf.square(y-pred), name='loss')
optm = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(cost)
# argmax()取最大值，1表示按行，0表示按列
corr = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accr = tf.reduce_mean(tf.cast(corr, 'float'))

init = tf.global_variables_initializer()
print('模型准备就绪')

training_epochs = 20
batch_size = 100
display_step = 4
sess = tf.Session()
sess.run(init)

for epoch in range(training_epochs):
    avg_cost = 0.
    total_batch = int(mnist.train.num_examples/batch_size)
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        feeds = {x: batch_xs, y: batch_ys}
        sess.run(optm, feed_dict=feeds)
        avg_cost += sess.run(cost, feed_dict=feeds)
    avg_cost /= total_batch
    if (epoch+1) % display_step == 0:
        print('epoch:%03d/%03d cost:%.9f' % (epoch, training_epochs, avg_cost))
        feeds_train = {x: batch_xs, y: batch_ys}
        train_acc = sess.run(accr, feed_dict=feeds)
        print("train acc:%3f" % train_acc)
        feeds = {x: mnist.test.images, y: mnist.test.labels}
        test_acc = sess.run(accr, feed_dict=feeds)
        print("test acc:%3f" % test_acc)
print("finish")




