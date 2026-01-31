"""
RNN Sequence Predictor
---------------------
This program uses a Recurrent Neural Network
to predict the next value in a sequence.

Author: AI Course
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


def main():
    print("RNN SEQUENCE PREDICTOR")
    print("-----------------------")

    # Generate sequence data
    # Example: [1,2,3] -> 4
    X = []
    y = []

    for i in range(1, 50):
        X.append([i, i+1, i+2])
        y.append(i+3)

    X = np.array(X)
    y = np.array(y)

    # Normalize
    X = X / 50.0
    y = y / 50.0

    # Reshape for RNN: (samples, time_steps, features)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Build RNN model
    model = models.Sequential([
        layers.SimpleRNN(32, activation="tanh", input_shape=(3, 1)),
        layers.Dense(1)
    ])

    # Compile model
    model.compile(
        optimizer="adam",
        loss="mse"
    )

    # Train model
    model.fit(X, y, epochs=100, batch_size=8)

    # Test prediction
    test_input = np.array([[47, 48, 49]]) / 50.0
    test_input = test_input.reshape((1, 3, 1))

    prediction = model.predict(test_input)

    print("\nPredicted next value:",
          round(prediction[0][0] * 50, 2))


if __name__ == "__main__":
    main()
