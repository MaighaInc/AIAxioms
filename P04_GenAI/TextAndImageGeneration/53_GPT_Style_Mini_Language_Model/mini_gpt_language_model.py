"""
Mini GPT-Style Language Model
-----------------------------
This program demonstrates how a GPT-like
decoder-only Transformer generates text.

Author: AI Course
"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np


class CausalSelfAttention(layers.Layer):
    def __init__(self, embed_dim):
        super().__init__()
        self.embed_dim = embed_dim
        self.query = layers.Dense(embed_dim)
        self.key = layers.Dense(embed_dim)
        self.value = layers.Dense(embed_dim)

    def call(self, x):
        q = self.query(x)
        k = self.key(x)
        v = self.value(x)

        scores = tf.matmul(q, k, transpose_b=True)
        mask = tf.linalg.band_part(tf.ones_like(scores), -1, 0)
        scores = scores * mask - 1e9 * (1 - mask)

        weights = tf.nn.softmax(scores, axis=-1)
        return tf.matmul(weights, v)


def main():
    print("MINI GPT-STYLE LANGUAGE MODEL")
    print("-----------------------------")

    text = "gpt models generate text intelligently "
    chars = sorted(set(text))

    char_to_idx = {c: i for i, c in enumerate(chars)}
    idx_to_char = {i: c for i, c in enumerate(chars)}

    vocab_size = len(chars)
    seq_len = 8

    X, y = [], []
    for i in range(len(text) - seq_len):
        X.append([char_to_idx[c] for c in text[i:i+seq_len]])
        y.append(char_to_idx[text[i+seq_len]])

    X = tf.keras.utils.to_categorical(X, vocab_size)
    y = tf.keras.utils.to_categorical(y, vocab_size)

    inputs = layers.Input(shape=(seq_len, vocab_size))
    x = CausalSelfAttention(embed_dim=32)(inputs)
    x = layers.Flatten()(x)
    outputs = layers.Dense(vocab_size, activation="softmax")(x)

    model = models.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="categorical_crossentropy")

    model.fit(X, y, epochs=200, verbose=0)

    seed = "gpt mode"
    generated = seed

    for _ in range(40):
        inp = [char_to_idx[c] for c in generated[-seq_len:]]
        inp = tf.keras.utils.to_categorical(inp, vocab_size)
        inp = inp.reshape(1, seq_len, vocab_size)

        preds = model.predict(inp, verbose=0)[0]
        generated += idx_to_char[np.argmax(preds)]

    print("\nGenerated Text:")
    print(generated)


if __name__ == "__main__":
    main()
