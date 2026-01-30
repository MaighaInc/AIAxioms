"""
Transfer Learning with ResNet
-----------------------------
This program demonstrates how to use a pretrained
ResNet model for image classification.

Author: AI Course
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.datasets import cifar10


def main():
    print("TRANSFER LEARNING WITH RESNET")
    print("------------------------------")

    # Load CIFAR-10 dataset
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    # Use only two classes for simplicity (airplane & automobile)
    X_train = X_train[y_train.flatten() < 2]
    y_train = y_train[y_train.flatten() < 2]
    X_test = X_test[y_test.flatten() < 2]
    y_test = y_test[y_test.flatten() < 2]

    # Resize images for ResNet (224x224)
    X_train = tf.image.resize(X_train, (224, 224)) / 255.0
    X_test = tf.image.resize(X_test, (224, 224)) / 255.0

    # Load pretrained ResNet50
    base_model = ResNet50(
        weights="imagenet",
        include_top=False,
        input_shape=(224, 224, 3)
    )

    base_model.trainable = False  # Freeze base model

    # Build model
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
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
    model.fit(X_train, y_train, epochs=5, batch_size=32)

    # Evaluate model
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print("\nTest Accuracy:", round(test_acc * 100, 2), "%")


if __name__ == "__main__":
    main()
