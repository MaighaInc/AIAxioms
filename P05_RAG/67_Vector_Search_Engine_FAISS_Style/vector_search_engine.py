"""
Vector Search Engine (FAISS-Style)
---------------------------------
This program searches for the most
similar documents using vector similarity.

Author: AI Course
"""

import math
from collections import Counter


class VectorSearchEngine:
    def tokenize(self, text):
        return text.lower().split()

    def build_vocabulary(self, texts):
        vocab = set()
        for text in texts:
            vocab.update(self.tokenize(text))
        return sorted(vocab)

    def embed(self, text, vocab):
        counts = Counter(self.tokenize(text))
        return [counts[word] for word in vocab]

    def cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        if mag1 == 0 or mag2 == 0:
            return 0
        return dot / (mag1 * mag2)

    def search(self, query, documents, top_k=2):
        vocab = self.build_vocabulary(documents + [query])
        doc_vectors = [self.embed(doc, vocab) for doc in documents]
        query_vector = self.embed(query, vocab)

        scores = []
        for doc, vec in zip(documents, doc_vectors):
            score = self.cosine_similarity(query_vector, vec)
            scores.append((doc, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]


def main():
    print("VECTOR SEARCH ENGINE")
    print("---------------------")

    documents = [
        "artificial intelligence is powerful",
        "machine learning builds intelligent systems",
        "deep learning is part of artificial intelligence",
        "football is a popular sport"
    ]

    search_engine = VectorSearchEngine()

    query = "intelligent systems and ai"
    results = search_engine.search(query, documents)

    print("\nQuery:", query)
    print("\nTop Results:")
    for doc, score in results:
        print(f"Score: {round(score, 3)} | Document: {doc}")


if __name__ == "__main__":
    main()
