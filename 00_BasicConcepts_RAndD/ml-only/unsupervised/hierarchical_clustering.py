from sklearn.cluster import AgglomerativeClustering

X = [[1], [2], [8], [9]]

model = AgglomerativeClustering(n_clusters=2)
print("Clusters:", model.fit_predict(X))
