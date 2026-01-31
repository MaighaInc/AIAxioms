```
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

```


from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

params = {"C": [0.1, 1, 10]}
model = GridSearchCV(SVC(), params)

X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model.fit(X, y)
print("Best params:", model.best_params_)
