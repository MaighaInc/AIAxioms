Algorithm: Bagging (Bootstrap Aggregation)

Goal:
Reduce variance of unstable models.

How it works:
- Train models on bootstrapped samples
- Aggregate predictions

Used With:
Decision Trees

Strengths:
- Reduces overfitting
- Parallelizable

Weaknesses:
- No bias reduction

Type:
Ensemble, Variance Reduction

****************************************************
Algorithm: AdaBoost

Goal:
Convert weak learners into strong learners.

How it works:
- Train models sequentially
- Increase weight of misclassified points

Key Idea:
Focus on hard examples.

Strengths:
- High accuracy
- Strong theoretical foundation

Weaknesses:
- Sensitive to noise
- Overfits with outliers

Type:
Ensemble, Boosting
