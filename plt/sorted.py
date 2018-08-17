import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter

k = 3
data_set = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
new_features = [4, 4]

distances = []
for group in data_set:
    for features in data_set[group]:
        euclidean_distance = np.linalg.norm(np.array(features) - np.array(new_features))
        distances.append([euclidean_distance, group])
print distances
print sorted(distances)
print sorted(distances)[:k]

votes = [i[1] for i in sorted(distances)[:k]]
print votes
print Counter(votes)
print Counter(votes).most_common(2)
for i in Counter(votes).most_common(2):
    print i
    for ii in i:
        print ii

