"""
Customer Churn Prediction using Scikit-learn
--------------------------------------------
This program predicts whether a customer
is likely to leave a service.

Author: AI Course
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    print("CUSTOMER CHURN PREDICTION MODEL")
    print("--------------------------------")

    # Dataset
    # Features: [Tenure, Monthly Charges, Total Charges, Support Calls, Contract Type]
    # Contract Type: 0 = Month-to-Month, 1 = Long-Term
    X = np.array([
        [1, 70, 70, 5, 0],
        [12, 60, 720, 1, 1],
        [3, 80, 240, 4, 0],
        [24, 55, 1320, 0, 1],
        [6, 75, 450, 3, 0],
        [36, 50, 1800, 0, 1],
        [2, 85, 170, 5, 0],
        [18, 58, 1044, 1, 1]
    ])

    # Labels: 1 = Churned, 0 = Retained
    y = np.array([1, 0, 1, 0, 1, 0, 1, 0])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)

    # Evaluation
    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))

    # Predict new customer
    new_customer = np.array([[4, 90, 360, 4, 0]])
    churn_prob = model.predict_proba(new_customer)

    print("\nNew Customer Churn Risk:")
    print("Churn Probability:", round(churn_prob[0][1], 2))
    print("Predicted Class:", model.predict(new_customer)[0])


if __name__ == "__main__":
    main()
