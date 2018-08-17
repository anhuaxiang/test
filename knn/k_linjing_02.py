# coding:utf-8
import warnings
import random
import numpy as np
import pandas as pd

from math import sqrt
from collections import Counter


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less than total voting groups!")

    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    # print Counter(votes).most_common(1)
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result


df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)  # 去掉id列
# print df
full_data = df.astype(float).values.tolist()  # 将数据转化为列表形式
# print full_data
random.shuffle(full_data)  # 打乱顺序
# print full_data

test_size = 0.2
train_set = {2: [], 4: []}
test_set = {2: [], 4: []}

# print len(full_data)
# print int(test_size * len(full_data))

train_data = full_data[:-int(test_size * len(full_data))]
test_data = full_data[-int(test_size) * len(full_data):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0
for group in test_set:
    for i in test_set[group]:
        result = k_nearest_neighbors(train_set, i, k=5)
        if result == group:
            correct += 1
        total += 1

print correct
print total
print correct*1.00/total



