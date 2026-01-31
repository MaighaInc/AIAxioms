from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

model = BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=5
)
model.fit(X, y)

print("Prediction:", model.predict([[2]]))
