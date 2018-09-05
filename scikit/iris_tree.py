from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree


iris = datasets.load_iris()
iris_data = iris['data']
iris_label = iris['target']
iris_target_name = iris['target_names']
x = np.array(iris_data)
y = np.array(iris_label)


clf = tree.DecisionTreeClassifier(max_depth=3)
clf.fit(x, y)

pri = clf.predict([7, 7, 7, 7])
print(pri)
