import matplotlib.pyplot as plt
from numpy import arange


X = [0, 1, 2, 3, 4, 5]
Y = [222, 42, 455, 664, 454, 334]
fig = plt.figure()

# plt.barh(X, Y, 0.5, 1, color="red")#横着
plt.bar(X, Y, 0.5, 1, color="red")#竖着

plt.show()
