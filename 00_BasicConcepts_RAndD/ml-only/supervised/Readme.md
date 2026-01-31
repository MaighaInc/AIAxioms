Algorithm: Linear Regression

Goal:
Learn a linear relationship between input features X and continuous output y.

Model:
y = wX + b

Objective:
Minimize Mean Squared Error (MSE):
MSE = (1/n) Σ(y_actual − y_predicted)²

Assumptions:
- Linearity
- Independence of errors
- Homoscedasticity
- No multicollinearity

Strengths:
- Simple, fast, interpretable
- Works well for linear trends

Weaknesses:
- Cannot model non-linear relationships
- Sensitive to outliers

Type:
Supervised, Parametric, Regression



***************************************************
Algorithm: Logistic Regression

Goal:
Binary classification using probabilities.

Model:
P(y=1) = sigmoid(wX + b)

Decision Boundary:
If probability ≥ threshold (usually 0.5), classify as class 1.

Loss Function:
Log Loss (Cross-Entropy)

Why "Regression":
It models probabilities, not class labels directly.

Strengths:
- Interpretable coefficients
- Probabilistic output

Weaknesses:
- Linear decision boundary
- Poor performance on complex data

Type:
Supervised, Parametric, Classification
************************************************************
Algorithm: k-Nearest Neighbors (k-NN)

Goal:
Classify a data point based on nearby labeled points.

How it works:
1. Compute distance to all points
2. Select k closest points
3. Majority vote (classification) or mean (regression)

Distance Metrics:
- Euclidean
- Manhattan
- Minkowski

Strengths:
- No training phase
- Simple and intuitive

Weaknesses:
- Slow for large datasets
- Sensitive to feature scaling

Type:
Supervised, Non-Parametric, Instance-Based
*****************************************************
Algorithm: Decision Tree

Goal:
Learn decision rules that split data into homogeneous regions.

How it works:
- Choose best feature split (Gini / Entropy)
- Recursively split until stopping condition

Key Concepts:
- Root, Node, Leaf
- Information Gain
- Overfitting risk

Strengths:
- Highly interpretable
- Handles non-linear data

Weaknesses:
- Overfits easily
- Unstable to small data changes

Type:
Supervised, Non-Parametric
***********************************************
Algorithm: Random Forest

Goal:
Improve decision trees using ensemble learning.

How it works:
- Train many decision trees
- Each tree sees random samples and features
- Final prediction = majority vote / average

Why it works:
Reduces variance of individual trees.

Strengths:
- High accuracy
- Resistant to overfitting

Weaknesses:
- Less interpretable
- More computational cost

Type:
Supervised, Ensemble (Bagging)
**************************************************

Algorithm: Support Vector Machine (SVM)

Goal:
Find a hyperplane that maximizes margin between classes.

Key Concepts:
- Support vectors
- Margin
- Kernel trick (linear, polynomial, RBF)

Objective:
Maximize margin while minimizing classification error.

Strengths:
- Effective in high-dimensional spaces
- Robust to overfitting

Weaknesses:
- Slow on large datasets
- Hard to tune

Type:
Supervised, Margin-Based
