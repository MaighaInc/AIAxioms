"""
Linear Regression From Scratch
------------------------------
This program learns a linear relationship
between input and output using gradient descent.

Author: AI Course
"""

class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weight = 0.0
        self.bias = 0.0

    def predict(self, x):
        return self.weight * x + self.bias

    def train(self, X, Y):
        n = len(X)

        for epoch in range(self.epochs):
            total_error = 0

            for x, y in zip(X, Y):
                prediction = self.predict(x)
                error = prediction - y

                # Gradient updates
                self.weight -= self.learning_rate * error * x
                self.bias -= self.learning_rate * error

                total_error += error ** 2

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {total_error / n:.4f}")


def main():
    print("LINEAR REGRESSION FROM SCRATCH")
    print("-------------------------------")

    # Sample dataset
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]

    model = LinearRegression(learning_rate=0.01, epochs=1000)
    model.train(X, Y)

    print("\nLearned Parameters:")
    print("Weight:", round(model.weight, 2))
    print("Bias:", round(model.bias, 2))

    test_value = 6
    prediction = model.predict(test_value)
    print(f"\nPrediction for x={test_value}:", prediction)


if __name__ == "__main__":
    main()
