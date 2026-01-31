"""
K-Means Customer Segmentation using Scikit-learn
------------------------------------------------
This program groups customers into clusters
based on behavior patterns.

Author: AI Course
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def main():
    print("K-MEANS CUSTOMER SEGMENTATION")
    print("------------------------------")

    # Dataset
    # Features: [Annual Income, Spending Score]
    X = np.array([
        [15, 39],
        [15, 81],
        [16, 6],
        [16, 77],
        [17, 40],
        [17, 76],
        [18, 6],
        [18, 94],
        [19, 3],
        [19, 72],
        [20, 14],
        [20, 90]
    ])

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)

    print("\nCluster Assignments:")
    for customer, cluster in zip(X, clusters):
        print(f"Customer {customer} -> Cluster {cluster}")

    # Cluster centers
    print("\nCluster Centers (Scaled Space):")
    print(kmeans.cluster_centers_)

    # New customer
    new_customer = np.array([[18, 65]])
    new_customer_scaled = scaler.transform(new_customer)
    new_cluster = kmeans.predict(new_customer_scaled)

    print("\nNew Customer:", new_customer[0])
    print("Assigned Cluster:", new_cluster[0])


if __name__ == "__main__":
    main()
