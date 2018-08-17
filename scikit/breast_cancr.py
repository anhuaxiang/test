import numpy as np
from sklearn import preprocessing, cross_validation, neighbors,svm
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

x = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
# clf = svm.SVC()
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)
print accuracy
sample = np.array([[1, 2, 5, 4, 2, 4, 6, 4, 4], [1, 2, 5, 4, 2, 4, 2, 4, 4]])
# sample = sample.reshape(2, -1)
print clf.predict(sample)



