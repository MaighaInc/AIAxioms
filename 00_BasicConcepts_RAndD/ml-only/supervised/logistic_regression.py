"""
Logistic Regression
Supervised | Parametric | Classification

Uses sigmoid function to estimate probabilities.
"""
from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = LogisticRegression()
model.fit(X,y)

print(model.predict([[3]]))
