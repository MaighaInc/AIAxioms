"""
Word2Vec Embedding Trainer (Skip-Gram)
-------------------------------------
This program trains word embeddings
from scratch using the Skip-Gram model.

Author: AI Course
"""

import numpy as np
from collections import defaultdict


class Word2Vec:
    def __init__(self, vocab_size, embedding_dim=10, lr=0.05):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.lr = lr

        self.W_in = np.random.randn(vocab_size, embedding_dim)
        self.W_out = np.random.randn(embedding_dim, vocab_size)

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / np.sum(exp_x)

    def train_pair(self, center_idx, context_idx):
        h = self.W_in[center_idx]
        scores = np.dot(h, self.W_out)
        y_pred = self.softmax(scores)

        error = y_pred
        error[context_idx] -= 1

        self.W_out -= self.lr * np.outer(h, error)
        self.W_in[center_idx] -= self.lr * np.dot(self.W_out, error)

    def train(self, pairs, epochs=100):
        for epoch in range(epochs):
            for center, context in pairs:
                self.train_pair(center, context)

    def get_embedding(self, idx):
        return self.W_in[idx]


def tokenize(text):
    return text.lower().split()


def main():
    print("WORD2VEC EMBEDDING TRAINER")
    print("---------------------------")

    corpus = [
        "deep learning is fun",
        "deep learning is powerful",
        "nlp is fun",
        "nlp and deep learning"
    ]

    tokens = []
    for sentence in corpus:
        tokens.extend(tokenize(sentence))

    vocab = list(set(tokens))
    word_to_idx = {word: i for i, word in enumerate(vocab)}

    # Generate skip-gram pairs
    window_size = 1
    pairs = []

    for sentence in corpus:
        words = tokenize(sentence)
        for i, word in enumerate(words):
            center = word_to_idx[word]
            for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
                if i != j:
                    context = word_to_idx[words[j]]
                    pairs.append((center, context))

    model = Word2Vec(vocab_size=len(vocab))
    model.train(pairs, epochs=200)

    print("\nWord Embeddings:")
    for word in vocab:
        print(word, "->", model.get_embedding(word_to_idx[word]))


if __name__ == "__main__":
    main()
