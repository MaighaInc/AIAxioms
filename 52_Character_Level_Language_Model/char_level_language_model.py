"""
Character-Level Language Model
------------------------------
This program trains a simple RNN to
generate text character by character.

Author: AI Course
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


def main():
    print("CHARACTER-LEVEL LANGUAGE MODEL")
    print("-------------------------------")

    # Training text (small on purpose)
    text = "generative ai creates new content. "

    # Build vocabulary
    chars = sorted(list(set(text)))
    char_to_idx = {c: i for i, c in enumerate(chars)}
    idx_to_char = {i: c for i, c in enumerate(chars)}

    vocab_size = len(chars)
    seq_len = 10

    # Prepare sequences
    X, y = [], []
    for i in range(len(text) - seq_len):
        X.append([char_to_idx[c] for c in text[i:i+seq_len]])
        y.append(char_to_idx[text[i+seq_len]])

    X = np.array(X)
    y = np.array(y)

    # One-hot encoding
    X = tf.keras.utils.to_categorical(X, num_classes=vocab_size)
    y = tf.keras.utils.to_categorical(y, num_classes=vocab_size)

    # Build model
    model = models.Sequential([
        layers.SimpleRNN(64, input_shape=(seq_len, vocab_size)),
        layers.Dense(vocab_size, activation="softmax")
    ])

    model.compile(optimizer="adam", loss="categorical_crossentropy")

    # Train
    model.fit(X, y, epochs=150, verbose=0)

    # Generate text
    seed = "generative"
    generated = seed

    for _ in range(50):
        inp = [char_to_idx[c] for c in generated[-seq_len:]]
        inp = tf.keras.utils.to_categorical(inp, num_classes=vocab_size)
        inp = inp.reshape(1, seq_len, vocab_size)

        preds = model.predict(inp, verbose=0)[0]
        next_char = idx_to_char[np.argmax(preds)]
        generated += next_char

    print("\nGenerated Text:")
    print(generated)


if __name__ == "__main__":
    main()
