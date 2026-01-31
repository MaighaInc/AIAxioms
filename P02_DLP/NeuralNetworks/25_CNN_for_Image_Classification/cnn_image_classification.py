"""
CNN for Image Classification (CIFAR-10)
---------------------------------------
This program classifies real-world images
using a Convolutional Neural Network.

Author: AI Course
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10


def main():
    print("CNN FOR IMAGE CLASSIFICATION")
    print("-----------------------------")

    # Load CIFAR-10 dataset
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    # Convert to binary classification
    # 0 = airplane, 1 = automobile (for simplicity)
    X_train = X_train[y_train.flatten() < 2]
    y_train = y_train[y_train.flatten() < 2]

    X_test = X_test[y_test.flatten() < 2]
    y_test = y_test[y_test.flatten() < 2]

    # Normalize images
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0

    # Build CNN model
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(1, activation="sigmoid")
    ])

    # Compile model
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    # Train model
    model.fit(X_train, y_train, epochs=10, batch_size=64)

    # Evaluate model
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print("\nTest Accuracy:", round(test_acc * 100, 2), "%")


if __name__ == "__main__":
    main()
