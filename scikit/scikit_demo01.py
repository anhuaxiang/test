# coding:utf-8

# 最小二乘法（预测值和实际值两者差的平方和最小）
import numpy as np
from sklearn import linear_model
from sklearn import svm

# clf = linear_model.LinearRegression()
# x_train = np.array([[0, 0], [1, 1], [2, 2]])
# y_train = np.array([0, 1, 2])
# clf.fit(x_train, y_train)
# print(clf.predict([0, 0]))
# print(clf.coef_)  # 获取W的值,线性中也就是一次项系数

# # 岭回归，在最小二乘法的基础上引入对系数大小进行惩罚的措施
# clf = linear_model.Ridge(alpha=0.5)
# x_train = np.array([[0, 0], [0, 0], [1, 1]])
# y_train = np.array([0, .1, 1])
# clf.fit(x_train, y_train)
# print(clf.coef_)
# print(clf.intercept_)  #截距

# 支持向量机
x = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(x, y)
print(clf.predict([[2, 2]]))
