"""
Cross Validation
Model Evaluation Technique
"""
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4]]
y = [2,4,6,8]

scores = cross_val_score(LinearRegression(), X, y, cv=2)
print(scores)
