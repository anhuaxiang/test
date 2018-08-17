import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

data_set = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
new_features_1 = [5, 7]
new_features_2 = [4, 4]


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less than total voting groups!")

    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    print Counter(votes).most_common(1)
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result


result_1 = k_nearest_neighbors(data_set, new_features_1, k=3)
print result_1

result_2 = k_nearest_neighbors(data_set, new_features_2, k=3)
print result_2

for i in data_set:
    for ii in data_set[i]:
        # euclidean_distance = np.linalg.norm(np.array(ii) - np.array(new_features))
        # print euclidean_distance
        plt.scatter(ii[0], ii[1], s=100, color=i)

plt.scatter(new_features_1[0], new_features_2[1], s=100, color="green")
plt.scatter(new_features_2[0], new_features_2[1], s=100, color="blue")

plt.show()
