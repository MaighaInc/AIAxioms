"""
Vector Embedding Generator
--------------------------
This program converts text into
numerical vector embeddings.

Author: AI Course
"""

import math
from collections import Counter


class VectorEmbeddingGenerator:
    def tokenize(self, text):
        return text.lower().split()

    def build_vocabulary(self, texts):
        vocab = set()
        for text in texts:
            vocab.update(self.tokenize(text))
        return sorted(vocab)

    def embed(self, text, vocabulary):
        tokens = self.tokenize(text)
        counts = Counter(tokens)
        vector = [counts[word] for word in vocabulary]
        return vector


def main():
    print("VECTOR EMBEDDING GENERATOR")
    print("---------------------------")

    documents = [
        "artificial intelligence is powerful",
        "machine learning builds intelligent systems",
        "deep learning is part of artificial intelligence"
    ]

    embedder = VectorEmbeddingGenerator()
    vocab = embedder.build_vocabulary(documents)

    print("\nVocabulary:")
    print(vocab)

    print("\nDocument Embeddings:")
    for doc in documents:
        vector = embedder.embed(doc, vocab)
        print(f"\nText: {doc}")
        print("Vector:", vector)


if __name__ == "__main__":
    main()
