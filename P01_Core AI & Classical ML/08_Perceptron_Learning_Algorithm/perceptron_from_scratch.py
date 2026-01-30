"""
Perceptron Learning Algorithm
----------------------------
This program implements a binary classifier
based on the Perceptron model.

Author: AI Course
"""

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=20):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = [0.0, 0.0]
        self.bias = 0.0

    def activation(self, x):
        """
        Step function
        """
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        """
        Predict class label
        """
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return self.activation(weighted_sum)

    def train(self, training_data):
        """
        Train perceptron using labeled data
        """
        for epoch in range(self.epochs):
            errors = 0
            for inputs, label in training_data:
                prediction = self.predict(inputs)
                error = label - prediction

                if error != 0:
                    self.weights = [
                        w + self.learning_rate * error * x
                        for w, x in zip(self.weights, inputs)
                    ]
                    self.bias += self.learning_rate * error
                    errors += 1

            print(f"Epoch {epoch}, Misclassifications: {errors}")
            if errors == 0:
                print("Training converged.")
                break


def main():
    print("PERCEPTRON LEARNING ALGORITHM")
    print("-----------------------------")

    # Linearly separable data
    training_data = [
        ([2, 1], 0),
        ([3, 2], 0),
        ([1, 1], 0),
        ([4, 5], 1),
        ([5, 6], 1),
        ([6, 5], 1)
    ]

    perceptron = Perceptron()
    perceptron.train(training_data)

    test_point = [3, 4]
    prediction = perceptron.predict(test_point)

    print("\nTest Point:", test_point)
    print("Prediction:", prediction)


if __name__ == "__main__":
    main()
