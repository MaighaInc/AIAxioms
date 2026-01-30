"""
Backpropagation From Scratch using NumPy
----------------------------------------
This program shows how neural networks
learn by propagating error backward.

Author: AI Course
"""

import numpy as np


class NeuralNetwork:
    def __init__(self, learning_rate=0.1):
        self.lr = learning_rate

        # Initialize weights and biases
        self.W1 = np.random.randn(2, 2)
        self.b1 = np.zeros((1, 2))

        self.W2 = np.random.randn(2, 1)
        self.b2 = np.zeros((1, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, a):
        return a * (1 - a)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)

        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.output = self.sigmoid(self.z2)

        return self.output

    def backward(self, X, y):
        m = X.shape[0]

        # Step 1: Output layer error
        error_output = self.output - y
        d_output = error_output * self.sigmoid_derivative(self.output)

        # Step 2: Gradients for W2 and b2
        dW2 = np.dot(self.a1.T, d_output) / m
        db2 = np.sum(d_output, axis=0, keepdims=True) / m

        # Step 3: Hidden layer error
        error_hidden = np.dot(d_output, self.W2.T)
        d_hidden = error_hidden * self.sigmoid_derivative(self.a1)

        # Step 4: Gradients for W1 and b1
        dW1 = np.dot(X.T, d_hidden) / m
        db1 = np.sum(d_hidden, axis=0, keepdims=True) / m

        # Step 5: Update parameters
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            predictions = self.forward(X)
            self.backward(X, y)

            if epoch % 100 == 0:
                loss = np.mean((predictions - y) ** 2)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        return (self.forward(X) > 0.5).astype(int)


def main():
    print("BACKPROPAGATION FROM SCRATCH")
    print("------------------------------")

    # XOR dataset
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([[0], [1], [1], [0]])

    model = NeuralNetwork(learning_rate=0.5)
    model.train(X, y, epochs=2000)

    predictions = model.predict(X)
    print("\nPredictions:")
    print(predictions)


if __name__ == "__main__":
    main()
