"""
Polynomial Regression From Scratch
----------------------------------
This program demonstrates how linear regression
can be extended to learn non-linear relationships
by using polynomial features.

Author: AI Course
"""

class PolynomialRegression:
    def __init__(self, learning_rate=0.01, epochs=3000, max_gradient=1.0):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.max_gradient = max_gradient
        self.w1 = 0.0   # coefficient for x
        self.w2 = 0.0   # coefficient for x^2
        self.bias = 0.0
        self.x_mean = 0.0
        self.x_std = 1.0
        self.y_mean = 0.0
        self.y_std = 1.0

    def _normalize(self, X, Y):
        """Normalize features and target for numerical stability"""
        import math
        
        # Calculate mean and std for X
        self.x_mean = sum(X) / len(X)
        variance_x = sum((x - self.x_mean) ** 2 for x in X) / len(X)
        self.x_std = math.sqrt(variance_x) if variance_x > 0 else 1.0
        
        # Calculate mean and std for Y
        self.y_mean = sum(Y) / len(Y)
        variance_y = sum((y - self.y_mean) ** 2 for y in Y) / len(Y)
        self.y_std = math.sqrt(variance_y) if variance_y > 0 else 1.0
        
        # Normalize
        X_norm = [(x - self.x_mean) / self.x_std for x in X]
        Y_norm = [(y - self.y_mean) / self.y_std for y in Y]
        
        return X_norm, Y_norm

    def _clip_gradient(self, gradient):
        """Clip gradient to prevent exploding gradients"""
        if gradient > self.max_gradient:
            return self.max_gradient
        elif gradient < -self.max_gradient:
            return -self.max_gradient
        return gradient

    def predict(self, x):
        """
        Polynomial prediction: y = w1*x + w2*x^2 + b
        """
        # Normalize input
        x_norm = (x - self.x_mean) / self.x_std
        # Predict on normalized scale
        y_norm = self.w1 * x_norm + self.w2 * (x_norm ** 2) + self.bias
        # Denormalize output
        return y_norm * self.y_std + self.y_mean

    def train(self, X, Y):
        # Normalize data
        X_norm, Y_norm = self._normalize(X, Y)
        n = len(X_norm)

        for epoch in range(self.epochs):
            total_loss = 0

            for x, y in zip(X_norm, Y_norm):
                prediction = self.w1 * x + self.w2 * (x ** 2) + self.bias
                error = prediction - y

                # Gradients
                dw1 = error * x
                dw2 = error * (x ** 2)
                db = error

                # Clip gradients to prevent overflow
                dw1 = self._clip_gradient(dw1)
                dw2 = self._clip_gradient(dw2)
                db = self._clip_gradient(db)

                # Update parameters
                self.w1 -= self.learning_rate * dw1
                self.w2 -= self.learning_rate * dw2
                self.bias -= self.learning_rate * db

                total_loss += error ** 2

            # Early stopping if loss becomes too large or NaN
            avg_loss = total_loss / n
            if avg_loss > 1e10 or avg_loss != avg_loss:  # Check for overflow or NaN
                print(f"Training stopped early at epoch {epoch} due to numerical instability")
                break

            if epoch % 500 == 0:
                print(f"Epoch {epoch}, Loss: {avg_loss:.4f}")


def main():
    print("POLYNOMIAL REGRESSION FROM SCRATCH")
    print("----------------------------------")

    # Dataset with curved relationship
    X = [1, 2, 3, 4, 5, 6]
    Y = [30, 40, 55, 60, 58, 50]

    model = PolynomialRegression()
    model.train(X, Y)

    print("\nLearned Parameters:")
    print("w1:", round(model.w1, 2))
    print("w2:", round(model.w2, 2))
    print("bias:", round(model.bias, 2))

    test_value = 4.5
    prediction = model.predict(test_value)
    print(f"\nPrediction for x={test_value}:", round(prediction, 2))


if __name__ == "__main__":
    main()
