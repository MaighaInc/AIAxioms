from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [6]]
y = [0, 0, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Class for 4:", model.predict([[4]]))
