from sklearn.svm import SVC

X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model = SVC(kernel="linear")
model.fit(X, y)

print("Prediction:", model.predict([[3]]))
