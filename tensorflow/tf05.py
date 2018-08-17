# coding:utf-8
import tensorflow as tf
import input_data

mnist = input_data.read_data_sets('data/', one_hot=True)
trainimg = mnist.train.images
trainlabel = mnist.train.labels
testimg = mnist.test.images
testlabel = mnist.test.labels
print("data ready")

# 28*28
n_input = 784
n_output = 10
stddev = 0.1
weight = {
    # 3*3， 1表示深度为1， 64表示输出，输出64个图
    'wc1': tf.Variable(tf.random_normal([3, 3, 1, 64], stddev=stddev)),
    'wc2': tf.Variable(tf.random_normal([3, 3, 64, 128], stddev=stddev)),
    # 经过一次2*2的池化后变为14*14，在经过一次2*2的池化后变为7*7
    'wd1': tf.Variable(tf.random_normal([7 * 7 * 128, 1024], stddev=stddev)),
    'wd2': tf.Variable(tf.random_normal([1024, n_output], stddev=stddev)),
}
biases = {
    'bc1': tf.Variable(tf.random_normal([64], stddev=stddev)),
    'bc2': tf.Variable(tf.random_normal([128], stddev=stddev)),
    'bd1': tf.Variable(tf.random_normal([1024], stddev=stddev)),
    'bd2': tf.Variable(tf.random_normal([n_output], stddev=stddev)),
}


# 卷积
def conv_basic(_input, _w, _b, _keepratio):
    # 变化数据的格式，标准4维
    _input_r = tf.reshape(_input, shape=[-1, 28, 28, 1])
    # 第一次卷积
    _conv1 = tf.nn.conv2d(_input_r, _w['wc1'], strides=[1, 1, 1, 1], padding='SAME')
    _conv1 = tf.nn.relu(tf.nn.bias_add(_conv1, _b['bc1']))
    # 第一次池化
    _pool1 = tf.nn.max_pool(_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    # 保留比列
    _pool_dr1 = tf.nn.dropout(_pool1, _keepratio)

    # 第二次卷积
    _conv2 = tf.nn.conv2d(_pool_dr1, _w['wc2'], strides=[1, 1, 1, 1], padding='SAME')
    _conv2 = tf.nn.relu(tf.nn.bias_add(_conv2, _b['bc2']))
    # 第二次池化
    _pool2 = tf.nn.max_pool(_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    # 比例保留
    _pool_dr2 = tf.nn.dropout(_pool2, _keepratio)

    # 全连接层
    # 转为一维向量形式
    _dense1 = tf.reshape(_pool_dr2, [-1, _w['wd1'].get_shape().as_list()[0]])
    # 第一次连接
    _fc1 = tf.nn.relu(tf.add(tf.matmul(_dense1, _w['wd1']), _b['bd1']))
    _fc_dr1 = tf.nn.dropout(_fc1, _keepratio)

    # 输出层
    _out = tf.add(tf.matmul(_fc_dr1, _w['wd2']), _b['bd2'])

    out = {
        'input_r': _input_r,
        'conv1': _conv1, 'pool1': _pool1, 'pool_dr1': _pool_dr1,
        'conv2': _conv2, 'pool2': _pool2, 'pool_dr2': _pool_dr2,
        'dense1': _dense1, 'fc1': _fc1, 'fc_dr1': _fc_dr1,
        'out': _out
    }
    return out
print('RNN ready')

x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_output])
keepratio = tf.placeholder(tf.float32)

_pred = conv_basic(x, weight, biases, keepratio)['out']
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=_pred))
optm = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
_coor = tf.equal(tf.argmax(_pred, 1), tf.argmax(y, 1))
accr = tf.reduce_mean(tf.cast(_coor, tf.float32))

init = tf.global_variables_initializer()
print("模型 ready")

sess = tf.Session()
sess.run(init)

training_epochs = 15
batch_size = 16
display_step = 3
for epoch in range(training_epochs):
    avg_cost = 0
    # total_batch = int(mnist.train.num_examples / batch_size)
    total_batch = 10
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        sess.run(optm, feed_dict={x: batch_xs, y: batch_ys, keepratio: 0.7})
        avg_cost += sess.run(cost, feed_dict={x: batch_xs, y: batch_ys, keepratio: 1.})/total_batch

    if epoch % display_step == 0:
        print('epoch:%03d/%03d  cost:%.9f' % (epoch, training_epochs, avg_cost))
        train_acc = sess.run(accr, feed_dict={x: batch_xs, y: batch_ys, keepratio: 1.})
        print('training acc:%.3f' % train_acc)
        test_acc = sess.run(accr, feed_dict={x: testimg, y: testlabel, keepratio: 1.})
        print('training acc:%.3f' % test_acc)
        print("*************************************")
