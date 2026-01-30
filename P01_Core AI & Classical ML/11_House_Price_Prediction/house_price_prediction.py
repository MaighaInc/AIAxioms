"""
House Price Prediction using Scikit-learn
-----------------------------------------
This program predicts house prices using
Linear Regression and real ML workflow.

Author: AI Course
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def main():
    print("HOUSE PRICE PREDICTION MODEL")
    print("-----------------------------")

    # Dataset
    # Features: [Size (sqft), Bedrooms, Age]
    X = np.array([
        [1000, 2, 10],
        [1200, 3, 5],
        [1500, 3, 8],
        [1800, 4, 3],
        [2000, 4, 2],
        [2300, 5, 1]
    ])

    # Target: Price in thousands
    y = np.array([200, 250, 300, 360, 400, 450])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Evaluation
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("Predictions:", predictions)
    print("RMSE:", round(rmse, 2))
    print("R2 Score:", round(r2, 2))

    # Feature importance
    print("\nFeature Coefficients:")
    for feature, coef in zip(["Size", "Bedrooms", "Age"], model.coef_):
        print(f"{feature}: {round(coef, 2)}")

    # New Prediction
    new_house = np.array([[1600, 3, 4]])
    predicted_price = model.predict(new_house)
    print("\nPredicted price for new house:", round(predicted_price[0], 2))


if __name__ == "__main__":
    main()
