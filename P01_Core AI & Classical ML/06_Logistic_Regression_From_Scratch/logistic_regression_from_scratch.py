"""
Logistic Regression From Scratch
--------------------------------
This program performs binary classification
using sigmoid function and gradient descent.

Author: AI Course
"""

import math


class LogisticRegression:
    def __init__(self, learning_rate=0.1, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weight = 0.0
        self.bias = 0.0

    def sigmoid(self, z):
        """
        Sigmoid activation function
        """
        return 1 / (1 + math.exp(-z))

    def predict_probability(self, x):
        """
        Predict probability of class 1
        """
        z = self.weight * x + self.bias
        return self.sigmoid(z)

    def predict(self, x):
        """
        Predict class label (0 or 1)
        """
        probability = self.predict_probability(x)
        return 1 if probability >= 0.5 else 0

    def train(self, X, Y):
        """
        Train logistic regression model
        """
        n = len(X)

        for epoch in range(self.epochs):
            total_loss = 0

            for x, y in zip(X, Y):
                prediction = self.predict_probability(x)

                # Log loss
                loss = -(y * math.log(prediction + 1e-9) +
                         (1 - y) * math.log(1 - prediction + 1e-9))
                total_loss += loss

                # Gradients
                error = prediction - y
                self.weight -= self.learning_rate * error * x
                self.bias -= self.learning_rate * error

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {total_loss / n:.4f}")


def main():
    print("LOGISTIC REGRESSION FROM SCRATCH")
    print("--------------------------------")

    # Dataset: hours studied vs pass/fail
    X = [1, 2, 3, 4, 5, 6]
    Y = [0, 0, 0, 1, 1, 1]

    model = LogisticRegression(learning_rate=0.1, epochs=1000)
    model.train(X, Y)

    print("\nLearned Parameters:")
    print("Weight:", round(model.weight, 2))
    print("Bias:", round(model.bias, 2))

    test_value = 3.5
    probability = model.predict_probability(test_value)
    prediction = model.predict(test_value)

    print(f"\nPrediction for x={test_value}:")
    print("Probability of Pass:", round(probability, 2))
    print("Predicted Class:", prediction)


if __name__ == "__main__":
    main()
