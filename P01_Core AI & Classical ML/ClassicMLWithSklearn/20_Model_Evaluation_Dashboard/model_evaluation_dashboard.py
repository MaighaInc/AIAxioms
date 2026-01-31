"""
Model Evaluation Dashboard
--------------------------
This program compares multiple ML models
using standard evaluation metrics.

Author: AI Course
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    return {
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(y_test, predictions),
        "Recall": recall_score(y_test, predictions),
        "F1 Score": f1_score(y_test, predictions)
    }


def main():
    print("MODEL EVALUATION DASHBOARD")
    print("---------------------------")

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
        [55, 100000, 760],
        [28, 32000, 610]
    ])

    # Labels: 1 = Approve Loan, 0 = Reject Loan
    y = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1, 0])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    # Train & Evaluate
    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        results[name] = evaluate_model(model, X_test, y_test)

    # Display Dashboard
    print("\nMODEL PERFORMANCE COMPARISON:\n")

    for model_name, metrics in results.items():
        print(model_name)
        print("-" * len(model_name))
        for metric, value in metrics.items():
            print(f"{metric}: {round(value, 2)}")
        print()


if __name__ == "__main__":
    main()
