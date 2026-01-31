"""
Image Classifier using MLP (From Scratch + NumPy)
------------------------------------------------
This program classifies handwritten digits
using a multilayer perceptron.

Author: AI Course
"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


class MLP:
    def __init__(self, input_size, hidden_size, output_size, lr=0.1):
        self.lr = lr

        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))

        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def relu(self, z):
        return np.maximum(0, z)

    def relu_derivative(self, z):
        return z > 0

    def softmax(self, z):
        exp = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp / np.sum(exp, axis=1, keepdims=True)

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.relu(self.z1)

        self.z2 = self.a1 @ self.W2 + self.b2
        self.output = self.softmax(self.z2)

        return self.output

    def backward(self, X, y):
        m = X.shape[0]

        dZ2 = self.output - y
        dW2 = self.a1.T @ dZ2 / m
        db2 = np.sum(dZ2, axis=0, keepdims=True) / m

        dA1 = dZ2 @ self.W2.T
        dZ1 = dA1 * self.relu_derivative(self.z1)
        dW1 = X.T @ dZ1 / m
        db1 = np.sum(dZ1, axis=0, keepdims=True) / m

        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y)

            if epoch % 100 == 0:
                loss = -np.mean(np.sum(y * np.log(self.output + 1e-9), axis=1))
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        probs = self.forward(X)
        return np.argmax(probs, axis=1)


def one_hot(y, num_classes):
    encoded = np.zeros((len(y), num_classes))
    encoded[np.arange(len(y)), y] = 1
    return encoded


def main():
    print("IMAGE CLASSIFIER USING MLP")
    print("---------------------------")

    digits = load_digits()
    X = digits.data / 16.0   # normalize
    y = digits.target

    y_encoded = one_hot(y, 10)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.3, random_state=42
    )

    model = MLP(
        input_size=64,
        hidden_size=64,
        output_size=10,
        lr=0.1
    )

    model.train(X_train, y_train, epochs=1000)

    predictions = model.predict(X_test)
    accuracy = np.mean(predictions == np.argmax(y_test, axis=1))

    print("\nTest Accuracy:", round(accuracy * 100, 2), "%")


if __name__ == "__main__":
    main()
