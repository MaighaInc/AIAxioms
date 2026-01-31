Algorithm: K-Means Clustering

Goal:
Group unlabeled data into k clusters.

How it works:
1. Initialize k centroids
2. Assign points to nearest centroid
3. Recompute centroids
4. Repeat until convergence

Objective:
Minimize Within-Cluster Sum of Squares (WCSS)

Strengths:
- Simple and fast
- Scales well

Weaknesses:
- Requires k beforehand
- Sensitive to initialization

Type:
Unsupervised, Partition-Based
************************************************************
Algorithm: Hierarchical Clustering

Goal:
Create a tree (dendrogram) of clusters.

Types:
- Agglomerative (bottom-up)
- Divisive (top-down)

Linkage Methods:
- Single
- Complete
- Average

Strengths:
- No need to specify k initially
- Interpretable hierarchy

Weaknesses:
- Computationally expensive
- Not scalable

Type:
Unsupervised, Hierarchical

**************************************************************
Algorithm: DBSCAN

Goal:
Discover clusters of arbitrary shape.

Key Parameters:
- eps: neighborhood radius
- min_samples: minimum points to form cluster

Core Idea:
Dense regions form clusters; sparse points are noise.

Strengths:
- Finds arbitrary shapes
- Handles outliers

Weaknesses:
- Parameter sensitive
- Struggles with varying densities

Type:
Unsupervised, Density-Based

************************************************************
Algorithm: Principal Component Analysis (PCA)

Goal:
Reduce dimensionality while preserving variance.

How it works:
- Compute covariance matrix
- Extract eigenvectors
- Project data onto top components

Properties:
- Linear transformation
- Components are orthogonal

Strengths:
- Reduces noise
- Improves visualization

Weaknesses:
- Loses interpretability
- Linear only

Type:
Unsupervised, Feature Extraction
