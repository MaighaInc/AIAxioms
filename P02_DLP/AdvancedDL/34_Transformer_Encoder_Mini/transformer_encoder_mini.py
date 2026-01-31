"""
Mini Transformer Encoder from Scratch (NumPy)
---------------------------------------------
This program implements a simplified Transformer
Encoder block using attention and feedforward layers.

Author: AI Course
"""

import numpy as np


def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)


def layer_norm(x, eps=1e-6):
    mean = np.mean(x)
    std = np.std(x)
    return (x - mean) / (std + eps)


def attention(Q, K, V):
    scores = np.dot(K, Q)
    weights = softmax(scores)
    return np.dot(weights, V)


def feed_forward(x, W1, W2):
    return np.dot(np.maximum(0, np.dot(x, W1)), W2)


def main():
    print("MINI TRANSFORMER ENCODER")
    print("-------------------------")

    # Input embeddings (3 tokens, embedding size 4)
    X = np.array([
        [1.0, 0.5, 0.2, 0.1],
        [0.9, 0.1, 0.3, 0.2],
        [0.8, 0.4, 0.4, 0.1]
    ])

    # Initialize weights
    Wq = np.random.randn(4, 4)
    Wk = np.random.randn(4, 4)
    Wv = np.random.randn(4, 4)

    W1 = np.random.randn(4, 8)
    W2 = np.random.randn(8, 4)

    outputs = []

    for x in X:
        Q = np.dot(x, Wq)
        K = np.dot(X, Wk)
        V = np.dot(X, Wv)

        attn_out = attention(Q, K, V)
        attn_residual = layer_norm(x + attn_out)

        ff_out = feed_forward(attn_residual, W1, W2)
        encoder_out = layer_norm(attn_residual + ff_out)

        outputs.append(encoder_out)

    outputs = np.array(outputs)

    print("\nEncoder Output:")
    print(outputs)


if __name__ == "__main__":
    main()
