"""
Feedforward Neural Network (From Scratch using NumPy)
-----------------------------------------------------
This program implements a simple neural network
with one hidden layer for binary classification.

Author: AI Course
"""

import numpy as np


class FeedForwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        self.learning_rate = learning_rate

        # Initialize weights and biases
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))

        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, a):
        return a * (1 - a)

    def forward(self, X):
        """
        Forward propagation
        """
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)

        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.output = self.sigmoid(self.z2)

        return self.output

    def backward(self, X, y):
        """
        Backpropagation
        """
        m = X.shape[0]

        error = self.output - y
        d_output = error * self.sigmoid_derivative(self.output)

        dW2 = np.dot(self.a1.T, d_output) / m
        db2 = np.sum(d_output, axis=0, keepdims=True) / m

        d_hidden = np.dot(d_output, self.W2.T) * self.sigmoid_derivative(self.a1)

        dW1 = np.dot(X.T, d_hidden) / m
        db1 = np.sum(d_hidden, axis=0, keepdims=True) / m

        # Update parameters
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            predictions = self.forward(X)
            self.backward(X, y)

            if epoch % 100 == 0:
                loss = np.mean((predictions - y) ** 2)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        predictions = self.forward(X)
        return (predictions > 0.5).astype(int)


def main():
    print("FEEDFORWARD NEURAL NETWORK (NUMPY)")
    print("----------------------------------")

    # Dataset: AND gate
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([[0], [0], [0], [1]])

    model = FeedForwardNeuralNetwork(
        input_size=2,
        hidden_size=4,
        output_size=1,
        learning_rate=0.5
    )

    model.train(X, y, epochs=2000)

    predictions = model.predict(X)

    print("\nPredictions:")
    print(predictions)


if __name__ == "__main__":
    main()
