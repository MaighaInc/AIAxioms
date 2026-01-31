"""
Gradient Boosting Classifier using Scikit-learn
-----------------------------------------------
This program demonstrates how gradient boosting
builds strong models by correcting previous mistakes.

Author: AI Course
"""

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    print("GRADIENT BOOSTING CLASSIFIER")
    print("-----------------------------")

    # Dataset
    # Features: [Age, Income, Credit Score, Loan Amount]
    X = np.array([
        [25, 30000, 600, 10000],
        [45, 80000, 750, 20000],
        [35, 50000, 680, 15000],
        [50, 90000, 720, 30000],
        [23, 20000, 590, 12000],
        [40, 70000, 710, 10000],
        [60, 120000, 780, 40000],
        [30, 40000, 650, 15000],
        [55, 100000, 760, 35000],
        [28, 32000, 610, 11000]
    ])

    # Labels: 1 = Approve Loan, 0 = Reject Loan
    y = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1, 0])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Model
    model = GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)

    # Evaluation
    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))

    # Feature importance
    print("\nFeature Importance:")
    for feature, importance in zip(
        ["Age", "Income", "Credit Score", "Loan Amount"],
        model.feature_importances_
    ):
        print(f"{feature}: {round(importance, 3)}")

    # New customer
    new_customer = np.array([[32, 45000, 660, 16000]])
    print("\nNew Customer Prediction:",
          model.predict(new_customer)[0])
    print("Approval Probability:",
          round(model.predict_proba(new_customer)[0][1], 2))


if __name__ == "__main__":
    main()
