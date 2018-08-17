import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("us.csv")
unrate['Date'] = pd.to_datetime(unrate["Date"])
# print (unrate.head())
# plt.plot(unrate["Date"], unrate["Unemployment Rate"])
plt.xticks(rotation=45)
# plt.xlabel("Month")
# plt.ylabel("Unemployee Rate")
# plt.title("Unemployee Rate")
# plt.show()

# fig = plt.figure(figsize=(6, 3))# 大图的尺寸
# a1 = fig.add_subplot(2, 2, 1)
# a2 = fig.add_subplot(2, 2, 2)
# a2 = fig.add_subplot(2, 2, 3)
# a2 = fig.add_subplot(2, 2, 4)
# a1.plot()

plt.plot(unrate[0:20]["Date"], unrate[0:20]["Unemployment Rate"], c="r")
plt.plot(unrate[20:40]["Date"], unrate[20:40]["Unemployment Rate"], c="b")
plt.legend(loc="best")

plt.show()