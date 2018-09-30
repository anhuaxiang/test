import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


features = pd.read_csv('Test1_features.dat', header=None)
labels = pd.read_csv('Test1_labels.dat', header=None)

x = np.array(features)
y = np.array(labels[0])

print(x.shape, y.shape)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(features, labels, test_size=0.2)

knn_classifier = KNeighborsClassifier()
bayes_classifier = GaussianNB()
dt_classifier = DecisionTreeClassifier()
svm_classifier = SVC(kernel='linear', C=0.4)

# # knn
# knn_classifier.fit(x_train, y_train)
# knn_score = knn_classifier.score(x_test, y_test)
# knn_acc = accuracy_score(y_test, knn_classifier.predict(x_test))
# print(f'knn----- score：{knn_score} acc: {knn_acc}')
#
# # 贝叶斯
# bayes_classifier.fit(x_train, y_train)
# bayes_acc = accuracy_score(y_test, bayes_classifier.predict(x_test))
# print(f'贝叶斯----- acc: {bayes_acc}')

# 决策树
dt_classifier.fit(x_train, y_train)
dt_score = dt_classifier.score(x_test, y_test)
dt_acc = accuracy_score(y_test, dt_classifier.predict(x_test))
print(f'决策树----- score：{dt_score} acc: {dt_acc}')

print(dt_classifier.max_depth, dt_classifier.max_features, dt_classifier.max_leaf_nodes)

# # 支持向量机
# svm_classifier.fit(x_train, y_train)
# pred_y = svm_classifier.predict(x_test)
# svm_acc = accuracy_score(y_test, pred_y)
# print(f'支持向量机----- acc: {svm_acc}')
# print(f'支持向量机 {classification_report(y_test, pred_y)}')
