import tensorflow as tf
import numpy as np

# help(tf)
# a = 1
# w = tf.Variable([[0.5, 1.0]])
# x = tf.Variable([[2.0], [1.0]])
#
# y = tf.matmul(w, x)
# print(y)
#
# # 全局初始化
# init_op = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init_op)
#     print(y.eval())
#     print(tf.zeros([2, 3]).eval())
#     print(tf.ones([2, 3]).eval())
#     # [1 2 3 4 5 6 7]
#     print(tf.constant([1, 2, 3, 4, 5, 6, 7]).eval())
#     # [10.0 11.0 12.0]
#     print(tf.linspace(10.0, 12.0, 3).eval())
#     # [ 3  6  9 12 15]
#     print(tf.range(3, 18, 3).eval())


# state = tf.Variable(0)
# new_value = tf.add(state, tf.constant(1))
# update = tf.assign(state, new_value)
# print(update)
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(state.eval())
#     for _ in range(3):
#         print(update.eval())
#
#     print("****************************")
#     print(sess.run(state))
#     for _ in range(5):
#         sess.run(update)
#         print(sess.run(state))


# import numpy as np
# a = np.zeros((3, 3))
# ta = tf.convert_to_tensor(a)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(ta))


# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
# output = tf.multiply(input1, input2)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run([output], feed_dict={input1: [7.], input2: [2.]}))


sess = tf.InteractiveSession()
arr = np.array([[31, 23, 4, 24, 27, 34],
                [18, 3, 25, 0, 6, 35],
                [28, 14, 33, 22, 20, 8],
                [13, 30, 21, 19, 7, 9],
                [16, 1, 26, 32, 2, 29],
                [17, 12, 5, 11, 10, 15]])
# 维数：2
print(tf.rank(arr).eval())
# 大小/行列：[6 6]
print(tf.shape(arr).eval())
# 返回最大值的索引：[0 3 2 4 0 1]，第二个参数0表示按列，1表示按行
print(tf.argmax(arr, 0).eval())
# [5 5 2 1 3 0]
print(tf.argmax(arr, 1).eval())
