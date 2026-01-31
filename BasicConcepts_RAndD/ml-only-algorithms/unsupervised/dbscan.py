from sklearn.cluster import DBSCAN

X = [[1], [2], [2], [8], [9]]

model = DBSCAN(eps=1.5, min_samples=2)
print("Clusters:", model.fit_predict(X))
