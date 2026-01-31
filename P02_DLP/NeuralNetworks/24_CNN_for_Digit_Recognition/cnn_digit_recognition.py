"""
CNN for Digit Recognition (MNIST)
---------------------------------
This program trains a Convolutional Neural Network
to recognize handwritten digits.

Author: AI Course
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist


def main():
    print("CNN FOR DIGIT RECOGNITION")
    print("--------------------------")

    # Load MNIST dataset
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Normalize and reshape
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0

    X_train = X_train.reshape(-1, 28, 28, 1)
    X_test = X_test.reshape(-1, 28, 28, 1)

    # Build CNN model
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(10, activation="softmax")
    ])

    # Compile model
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    # Train model
    model.fit(X_train, y_train, epochs=5, batch_size=64)

    # Evaluate model
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print("\nTest Accuracy:", round(test_acc * 100, 2), "%")


if __name__ == "__main__":
    main()
