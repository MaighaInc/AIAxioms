"""
Random Forest Classifier using Scikit-learn
-------------------------------------------
This program demonstrates how multiple decision trees
work together to make better predictions.

Author: AI Course
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    print("RANDOM FOREST CLASSIFIER")
    print("------------------------")

    # Dataset
    # Features: [Age, Income, Credit Score]
    X = np.array([
        [25, 30000, 600],
        [45, 80000, 750],
        [35, 50000, 680],
        [50, 90000, 720],
        [23, 20000, 590],
        [40, 70000, 710],
        [60, 120000, 780],
        [30, 40000, 650],
        [55, 100000, 760]
    ])

    # Labels: 1 = Approve Loan, 0 = Reject Loan
    y = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
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
        ["Age", "Income", "Credit Score"],
        model.feature_importances_
    ):
        print(f"{feature}: {round(importance, 3)}")

    # New prediction
    new_customer = np.array([[28, 35000, 640]])
    print("\nNew Customer Prediction:",
          model.predict(new_customer)[0])
    print("Approval Probability:",
          round(model.predict_proba(new_customer)[0][1], 2))


if __name__ == "__main__":
    main()
