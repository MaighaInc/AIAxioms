"""
GloVe-style Word Embeddings (From Scratch)
-----------------------------------------
This program demonstrates how global
word co-occurrence statistics are used
to learn word embeddings.

Author: AI Course
"""

import numpy as np
from collections import defaultdict


class GloVe:
    def __init__(self, vocab_size, embedding_dim=10, lr=0.05):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.lr = lr

        self.W = np.random.randn(vocab_size, embedding_dim)
        self.W_tilde = np.random.randn(vocab_size, embedding_dim)
        self.b = np.zeros(vocab_size)
        self.b_tilde = np.zeros(vocab_size)

    def train(self, cooccurrence, epochs=100):
        for epoch in range(epochs):
            total_loss = 0
            for (i, j), count in cooccurrence.items():
                weight = min(1.0, count / 10)
                dot = np.dot(self.W[i], self.W_tilde[j])
                loss = weight * ((dot + self.b[i] + self.b_tilde[j] - np.log(count)) ** 2)

                grad = weight * 2 * (dot + self.b[i] + self.b_tilde[j] - np.log(count))

                self.W[i] -= self.lr * grad * self.W_tilde[j]
                self.W_tilde[j] -= self.lr * grad * self.W[i]
                self.b[i] -= self.lr * grad
                self.b_tilde[j] -= self.lr * grad

                total_loss += loss

            if epoch % 20 == 0:
                print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

    def get_embedding(self, idx):
        return self.W[idx] + self.W_tilde[idx]


def tokenize(text):
    return text.lower().split()


def main():
    print("GLOVE-STYLE WORD EMBEDDINGS")
    print("----------------------------")

    corpus = [
        "deep learning is powerful",
        "deep learning is fun",
        "nlp is powerful",
        "nlp and deep learning"
    ]

    tokens = []
    for sentence in corpus:
        tokens.extend(tokenize(sentence))

    vocab = list(set(tokens))
    word_to_idx = {word: i for i, word in enumerate(vocab)}

    # Build co-occurrence matrix
    window_size = 2
    cooccurrence = defaultdict(int)

    for sentence in corpus:
        words = tokenize(sentence)
        for i, word in enumerate(words):
            for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
                if i != j:
                    cooccurrence[(word_to_idx[word], word_to_idx[words[j]])] += 1

    model = GloVe(vocab_size=len(vocab))
    model.train(cooccurrence, epochs=100)

    print("\nWord Embeddings:")
    for word in vocab:
        print(word, "->", model.get_embedding(word_to_idx[word]))


if __name__ == "__main__":
    main()
