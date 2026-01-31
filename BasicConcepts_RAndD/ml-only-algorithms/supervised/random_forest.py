from sklearn.ensemble import RandomForestClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

print("Prediction:", model.predict([[2]]))
