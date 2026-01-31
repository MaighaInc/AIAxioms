import numpy as np
from sklearn.decomposition import PCA

X = np.array([[1, 2], [3, 4], [5, 6]])

pca = PCA(n_components=1)
X_reduced = pca.fit_transform(X)

print("Reduced data:", X_reduced)
