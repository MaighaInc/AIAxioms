"""
AdaBoost
Ensemble | Boosting

Sequentially focuses on misclassified samples.
"""
from sklearn.ensemble import AdaBoostClassifier

X = [[0],[1],[2],[3]]
y = [0,0,1,1]

model = AdaBoostClassifier(n_estimators=10)
model.fit(X,y)

print(model.predict([[2]]))
