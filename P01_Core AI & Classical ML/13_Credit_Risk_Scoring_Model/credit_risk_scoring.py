"""
Credit Risk Scoring Model using Scikit-learn
--------------------------------------------
This program predicts whether a customer
is likely to default on a loan.

Author: AI Course
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    print("CREDIT RISK SCORING MODEL")
    print("-------------------------")

    # Dataset
    # Features: [Age, Income, Loan Amount, Credit Score]
    X = np.array([
        [25, 30000, 10000, 600],
        [45, 80000, 20000, 750],
        [35, 50000, 15000, 680],
        [50, 90000, 30000, 720],
        [23, 20000, 12000, 590],
        [40, 70000, 10000, 710],
        [60, 120000, 40000, 780]
    ])

    # Labels: 0 = High Risk, 1 = Low Risk
    y = np.array([0, 1, 0, 1, 0, 1, 1])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)

    # Evaluation
    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))

    # New customer prediction
    new_customer = np.array([[30, 40000, 15000, 650]])
    risk_prob = model.predict_proba(new_customer)

    print("\nNew Customer Risk Probability:")
    print("Low Risk Probability:", round(risk_prob[0][1], 2))
    print("Predicted Class:", model.predict(new_customer)[0])


if __name__ == "__main__":
    main()
