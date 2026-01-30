"""
LSTM Text Generator
-------------------
This program trains an LSTM network
to generate text character by character.

Author: AI Course
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


def main():
    print("LSTM TEXT GENERATOR")
    print("-------------------")

    # Training text (small on purpose for teaching)
    text = "deep learning is powerful and exciting. "

    # Create character vocabulary
    chars = sorted(list(set(text)))
    char_to_idx = {c: i for i, c in enumerate(chars)}
    idx_to_char = {i: c for i, c in enumerate(chars)}

    vocab_size = len(chars)
    seq_length = 10

    # Prepare training data
    X = []
    y = []

    for i in range(len(text) - seq_length):
        X.append([char_to_idx[c] for c in text[i:i+seq_length]])
        y.append(char_to_idx[text[i+seq_length]])

    X = np.array(X)
    y = np.array(y)

    # One-hot encode
    X = tf.keras.utils.to_categorical(X, num_classes=vocab_size)
    y = tf.keras.utils.to_categorical(y, num_classes=vocab_size)

    # Build LSTM model
    model = models.Sequential([
        layers.LSTM(128, input_shape=(seq_length, vocab_size)),
        layers.Dense(vocab_size, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy"
    )

    # Train model
    model.fit(X, y, epochs=200, verbose=0)

    # Text generation
    seed_text = "deep learn"
    generated = seed_text

    for _ in range(50):
        input_seq = [char_to_idx[c] for c in generated[-seq_length:]]
        input_seq = tf.keras.utils.to_categorical(
            input_seq, num_classes=vocab_size
        )
        input_seq = input_seq.reshape(1, seq_length, vocab_size)

        prediction = model.predict(input_seq, verbose=0)
        next_char_idx = np.argmax(prediction)
        generated += idx_to_char[next_char_idx]

    print("\nGenerated Text:")
    print(generated)


if __name__ == "__main__":
    main()
