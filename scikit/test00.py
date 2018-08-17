from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[140, 1]])
print clf.predict([[130, 1]])
print clf.predict([[150, 0]])
print clf.predict([[170, 0]])
