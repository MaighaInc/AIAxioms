"""
PCA - Dimensionality Reduction using Scikit-learn
------------------------------------------------
This program reduces high-dimensional data
into lower dimensions while retaining
maximum information.

Author: AI Course
"""

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np


def main():
    print("PCA DIMENSIONALITY REDUCTION")
    print("----------------------------")

    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names

    print("\nOriginal Data Shape:", X.shape)

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    print("Reduced Data Shape:", X_pca.shape)

    # Explained variance
    explained_variance = pca.explained_variance_ratio_

    print("\nExplained Variance Ratio:")
    for i, var in enumerate(explained_variance):
        print(f"Principal Component {i+1}: {round(var*100,2)}%")

    print("\nTotal Variance Retained:",
          round(sum(explained_variance) * 100, 2), "%")

    # Show PCA components
    print("\nPCA Components (Feature Contributions):")
    for i, component in enumerate(pca.components_):
        print(f"\nComponent {i+1}:")
        for feature, value in zip(feature_names, component):
            print(f"{feature}: {round(value, 3)}")


if __name__ == "__main__":
    main()
