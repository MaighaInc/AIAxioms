"""
Variational Autoencoder (VAE)
-----------------------------
This program demonstrates how a VAE learns
a probabilistic latent space and generates data.

Author: AI Course
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


# Sampling function (reparameterization trick)
def sampling(args):
    z_mean, z_log_var = args
    epsilon = tf.random.normal(shape=tf.shape(z_mean))
    return z_mean + tf.exp(0.5 * z_log_var) * epsilon


def main():
    print("VARIATIONAL AUTOENCODER")
    print("------------------------")

    # Generate simple data
    X = np.random.normal(size=(1000, 2))
    X = X.astype("float32")

    # Encoder
    inputs = layers.Input(shape=(2,))
    h = layers.Dense(16, activation="relu")(inputs)
    z_mean = layers.Dense(2)(h)
    z_log_var = layers.Dense(2)(h)
    z = layers.Lambda(sampling)([z_mean, z_log_var])

    encoder = models.Model(inputs, [z_mean, z_log_var, z])

    # Decoder
    latent_inputs = layers.Input(shape=(2,))
    h_dec = layers.Dense(16, activation="relu")(latent_inputs)
    outputs = layers.Dense(2)(h_dec)

    decoder = models.Model(latent_inputs, outputs)

    # VAE model
    outputs = decoder(encoder(inputs)[2])
    vae = models.Model(inputs, outputs)

    # Loss function
    reconstruction_loss = tf.reduce_mean(
        tf.square(inputs - outputs)
    )

    kl_loss = -0.5 * tf.reduce_mean(
        1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var)
    )

    vae.add_loss(reconstruction_loss + kl_loss)

    vae.compile(optimizer="adam")

    # Train VAE
    vae.fit(X, X, epochs=50, batch_size=32)

    # Generate new data
    new_points = decoder.predict(np.random.normal(size=(5, 2)))
    print("\nGenerated samples:")
    print(new_points)


if __name__ == "__main__":
    main()
