"""
K-Means Clustering
Unsupervised | Partition-based

Minimizes within-cluster sum of squares.
"""
from sklearn.cluster import KMeans

X = [[1],[2],[8],[9]]
model = KMeans(n_clusters=2, n_init=10)
model.fit(X)

print(model.labels_)
