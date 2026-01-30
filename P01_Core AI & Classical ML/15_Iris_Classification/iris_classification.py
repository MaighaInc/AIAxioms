"""
Iris Flower Classification using Scikit-learn
---------------------------------------------
This program classifies iris flowers
into three species using Logistic Regression.

Author: AI Course
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    print("IRIS FLOWER CLASSIFICATION")
    print("--------------------------")

    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Evaluation
    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n",
          classification_report(y_test, predictions, target_names=target_names))

    # Predict new flower
    new_flower = [[5.1, 3.5, 1.4, 0.2]]
    predicted_class = model.predict(new_flower)

    print("\nNew Flower Measurements:", new_flower[0])
    print("Predicted Species:", target_names[predicted_class[0]])


if __name__ == "__main__":
    main()
