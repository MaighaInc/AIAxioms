from sklearn.naive_bayes import GaussianNB

X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model = GaussianNB()
model.fit(X, y)

print("Prediction:", model.predict([[3]]))
