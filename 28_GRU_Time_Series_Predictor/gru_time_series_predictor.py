"""
GRU Time-Series Predictor
-------------------------
This program uses a GRU network
to predict the next value in a time series.

Author: AI Course
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


def main():
    print("GRU TIME-SERIES PREDICTOR")
    print("--------------------------")

    # Generate time-series data
    X = []
    y = []

    for i in range(1, 100):
        X.append([i, i+1, i+2, i+3])
        y.append(i+4)

    X = np.array(X)
    y = np.array(y)

    # Normalize
    X = X / 100.0
    y = y / 100.0

    # Reshape for GRU: (samples, timesteps, features)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Build GRU model
    model = models.Sequential([
        layers.GRU(64, input_shape=(4, 1)),
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
    test_input = np.array([[96, 97, 98, 99]]) / 100.0
    test_input = test_input.reshape((1, 4, 1))

    prediction = model.predict(test_input)

    print("\nPredicted next value:",
          round(prediction[0][0] * 100, 2))


if __name__ == "__main__":
    main()
