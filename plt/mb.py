# _*_coding:utf-8 _*_
from statistics import mean
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


# 生成随机测试数集
def create_data_set(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation =="pos":
            val +=step
        elif correlation and correlation =="neg":
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

# 求m, b
def best_fit_slope(xs, ys):
    m = ((mean(xs) * mean(ys) - mean(xs * ys)) / (mean(xs) * mean(xs) - mean(xs * xs)))
    b = mean(ys) - m * mean(xs)
    return m, b


# y=mx+x
def y_value(x, m, b):
    y_list = []
    for x_each in x:
        y_each = m * x_each + b
        y_list.append(y_each)
    return y_list


# 误差的平方和
def squard_errors(ys_orig, ys_line):
    return sum((ys_line - ys_orig) ** 2)


# R^2
def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squard_errors_regr = squard_errors(ys_orig, ys_line)
    squard_errors_y_mean = squard_errors(ys_orig, y_mean_line)
    return 1 - (squard_errors_regr / squard_errors_y_mean)

xs, ys = create_data_set(40, 34, 2, correlation="pos")

m, b = best_fit_slope(xs, ys)
print("m=",m,",b=",b)

regression_line = [(m*x) + b for x in xs]
r_squared = coefficient_of_determination(ys, regression_line)
print("r^2=",r_squared)

plt.scatter(xs, ys)

y_test = y_value(xs, m, b)
# # 或者 y = [m*x+b for x in x_test]
plt.plot(xs, y_test)

pre_x = 23
pre_y = m * pre_x + b
plt.scatter(pre_x, pre_y, s=100, color='r')
plt.show()
