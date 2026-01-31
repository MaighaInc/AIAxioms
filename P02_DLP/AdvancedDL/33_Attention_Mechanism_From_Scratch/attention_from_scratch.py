"""
Attention Mechanism from Scratch (NumPy)
----------------------------------------
This program demonstrates how attention works
using Query, Key, and Value vectors.

Author: AI Course
"""

import numpy as np


def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)


def attention(query, keys, values):
    """
    Scaled Dot-Product Attention
    """
    scores = np.dot(keys, query)
    weights = softmax(scores)
    output = np.dot(weights, values)
    return output, weights


def main():
    print("ATTENTION MECHANISM FROM SCRATCH")
    print("--------------------------------")

    # Example word embeddings (simplified)
    keys = np.array([
        [1, 0, 1],
        [0, 2, 0],
        [1, 1, 0]
    ])

    values = np.array([
        [10, 0],
        [0, 10],
        [5, 5]
    ])

    # Query vector (what we are focusing on)
    query = np.array([1, 1, 0])

    output, weights = attention(query, keys, values)

    print("\nAttention Weights:")
    print(weights)

    print("\nAttention Output:")
    print(output)


if __name__ == "__main__":
    main()
