"""
Linear Regression
Supervised | Parametric | Regression

Objective:
Minimize Mean Squared Error between predicted and actual values.
"""
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4]])
y = np.array([2,4,6,8])

model = LinearRegression()
model.fit(X, y)

print(model.predict([[5]]))
