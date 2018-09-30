import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import StratifiedKFold, KFold

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

features = pd.read_csv('Test1_features.dat', header=None)
labels = pd.read_csv('Test1_labels.dat', header=None)
x = np.array(features)
y = np.array(labels[0])
print(x.shape)
print(y.shape)

decision_tree_classifier = DecisionTreeClassifier()
parameter_grid = {
    'max_depth': list(range(55, 65, 1)),  # 55, 65, 1
    'max_features': list(range(45, 62, 1)),  # 45, 62, 1
}
cross_validation = StratifiedKFold(n_splits=3)
grid_search = GridSearchCV(decision_tree_classifier, param_grid=parameter_grid, cv=3)

grid_search.fit(x, y)
best_param = grid_search.best_params_

print('best_params', grid_search.best_params_)
print('grid_scores', grid_search.grid_scores_)
print('best_score', grid_search.best_score_)

r_x = []
r_y = []
r_z = []
for i in grid_search.grid_scores_:
    r_x.append(i[0]['max_depth'])
    r_y.append(i[0]['max_features'])
    r_z.append(i[1])

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('max_depth')
ax.set_ylabel('max_features')
ax.set_zlabel('score')
# r_x, r_y = np.meshgrid(r_x, r_y)
# r_z = np.array(r_z)
# r_z = np.atleast_2d(r_z)
# ax.plot_surface(r_x, r_y, r_z, rstride=1, cstride=1, cmap='rainbow')
ax.scatter(r_x, r_y, r_z, c='g')
plt.show()


# best_decision_tree_classifier = DecisionTreeClassifier(max_depth=best_param['max_depth'],
#                                                        max_features=best_param['max_features'])
# print(accuracy_score(y, best_decision_tree_classifier.predict(x)))
