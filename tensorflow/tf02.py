import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# 随机生成1000个数据点，标准为y=0.1x+0.3
num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]
plt.scatter(x_data, y_data, c='r')
# plt.show()

# 生成一维w
w = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name='w')
# 生成一维b
b = tf.Variable(tf.zeros([1]), name='b')
# 回归公式
y = w * x_data + b

# 以预估值y和实际值y_data之间的平均方误差作为损失值
loss = tf.reduce_mean(tf.square(y-y_data), name='loss')
# 采用梯度下降的方法来训练参数
optimizer = tf.train.GradientDescentOptimizer(0.5)
# 训练的过程就是最小化误差值
train = optimizer.minimize(loss, name='train')

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

print("w=", sess.run(w), "b=", sess.run(b), "loss=", sess.run(loss))
for step in range(50):
    sess.run(train)
    print("w=", sess.run(w), "b=", sess.run(b), "loss=", sess.run(loss))
w1 = sess.run(w)[0]
b1 = sess.run(b)[0]

plt.plot(x_data, [x * w1 + b1 for x in x_data])
plt.plot(x_data, [x * 0.1 + 0.3 for x in x_data], c="y")

plt.show()
