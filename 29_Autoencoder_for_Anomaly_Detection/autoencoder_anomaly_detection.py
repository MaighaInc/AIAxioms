"""
Autoencoder for Anomaly Detection
---------------------------------
This program detects anomalies by learning
normal patterns and measuring reconstruction error.

Author: AI Course
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


def main():
    print("AUTOENCODER FOR ANOMALY DETECTION")
    print("--------------------------------")

    # Generate normal data (normal behavior)
    normal_data = np.random.normal(loc=0, scale=1, size=(1000, 10))

    # Generate anomalous data (abnormal behavior)
    anomaly_data = np.random.normal(loc=5, scale=1, size=(50, 10))

    # Autoencoder model
    model = models.Sequential([
        layers.Dense(6, activation="relu", input_shape=(10,)),
        layers.Dense(3, activation="relu"),
        layers.Dense(6, activation="relu"),
        layers.Dense(10)
    ])

    model.compile(
        optimizer="adam",
        loss="mse"
    )

    # Train only on normal data
    model.fit(
        normal_data,
        normal_data,
        epochs=50,
        batch_size=32,
        verbose=0
    )

    # Reconstruction error
    reconstructed_normal = model.predict(normal_data)
    reconstructed_anomaly = model.predict(anomaly_data)

    normal_error = np.mean(
        np.square(normal_data - reconstructed_normal),
        axis=1
    )

    anomaly_error = np.mean(
        np.square(anomaly_data - reconstructed_anomaly),
        axis=1
    )

    print("\nAverage reconstruction error:")
    print("Normal data:", round(np.mean(normal_error), 4))
    print("Anomaly data:", round(np.mean(anomaly_error), 4))

    # Simple threshold
    threshold = np.mean(normal_error) + 2 * np.std(normal_error)

    detected = anomaly_error > threshold
    print("\nAnomalies detected:", np.sum(detected), "out of", len(anomaly_data))


if __name__ == "__main__":
    main()
