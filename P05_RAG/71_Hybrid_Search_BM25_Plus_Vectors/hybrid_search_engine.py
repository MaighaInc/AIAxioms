"""
Hybrid Search Engine (BM25 + Vector Similarity)
----------------------------------------------
This program combines keyword-based
search with semantic vector search.

Author: AI Course
"""

import math
from collections import Counter


class HybridSearchEngine:
    def tokenize(self, text):
        return text.lower().split()

    # ---------- BM25 STYLE ----------
    def bm25_score(self, query_tokens, doc_tokens, k1=1.5, b=0.75):
        score = 0.0
        doc_len = len(doc_tokens)
        avg_doc_len = doc_len  # simplified for demo
        freq = Counter(doc_tokens)

        for term in query_tokens:
            if term in freq:
                tf = freq[term]
                score += ((tf * (k1 + 1)) /
                          (tf + k1 * (1 - b + b * doc_len / avg_doc_len)))
        return score

    # ---------- VECTOR SEARCH ----------
    def embed(self, tokens, vocab):
        counts = Counter(tokens)
        return [counts[word] for word in vocab]

    def cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        if mag1 == 0 or mag2 == 0:
            return 0.0
        return dot / (mag1 * mag2)

    def search(self, query, documents, top_k=3):
        query_tokens = self.tokenize(query)

        # Build vocabulary for vectors
        vocab = set(query_tokens)
        for doc in documents:
            vocab.update(self.tokenize(doc))
        vocab = list(vocab)

        query_vec = self.embed(query_tokens, vocab)

        results = []
        for doc in documents:
            doc_tokens = self.tokenize(doc)
            bm25 = self.bm25_score(query_tokens, doc_tokens)
            doc_vec = self.embed(doc_tokens, vocab)
            vector_score = self.cosine_similarity(query_vec, doc_vec)

            hybrid_score = bm25 + vector_score
            results.append((doc, hybrid_score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]


def main():
    print("HYBRID SEARCH ENGINE")
    print("---------------------")

    documents = [
        "Artificial intelligence and machine learning systems",
        "Deep learning uses neural networks",
        "Football is a popular sport worldwide",
        "Machine learning improves AI systems"
    ]

    search_engine = HybridSearchEngine()

    query = "machine learning systems"
    results = search_engine.search(query, documents)

    print("\nQuery:", query)
    print("\nTop Results:")
    for doc, score in results:
        print(f"Score: {round(score, 3)} | Document: {doc}")


if __name__ == "__main__":
    main()
