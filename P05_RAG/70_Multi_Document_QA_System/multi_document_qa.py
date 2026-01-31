"""
Multi-Document QA System
-----------------------
This program answers a question by
retrieving relevant chunks across
multiple documents.

Author: AI Course
"""

import math
from collections import Counter, defaultdict


class Embedder:
    def tokenize(self, text):
        return text.lower().split()

    def embed(self, text, vocab):
        counts = Counter(self.tokenize(text))
        return [counts[word] for word in vocab]


class MultiDocumentQA:
    def cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        if mag1 == 0 or mag2 == 0:
            return 0.0
        return dot / (mag1 * mag2)

    def retrieve(self, query, documents, top_k=3):
        embedder = Embedder()

        # Build vocabulary from all docs + query
        vocab = set()
        for doc_name, chunks in documents.items():
            for chunk in chunks:
                vocab.update(embedder.tokenize(chunk))
        vocab.update(embedder.tokenize(query))
        vocab = list(vocab)

        query_vec = embedder.embed(query, vocab)

        scored = []
        for doc_name, chunks in documents.items():
            for chunk in chunks:
                chunk_vec = embedder.embed(chunk, vocab)
                score = self.cosine_similarity(query_vec, chunk_vec)
                scored.append((doc_name, chunk, score))

        scored.sort(key=lambda x: x[2], reverse=True)
        return scored[:top_k]

    def generate_answer(self, question, retrieved_items):
        context = "\n".join(
            f"[{doc}] {chunk}"
            for doc, chunk, _ in retrieved_items
        )
        return f"Answer based on multiple documents:\n{context}"

    def ask(self, question, documents):
        retrieved = self.retrieve(question, documents)
        return self.generate_answer(question, retrieved)


def main():
    print("MULTI-DOCUMENT QA SYSTEM")
    print("-------------------------")

    documents = {
        "doc1_ai.txt": [
            "Artificial intelligence enables machines to learn.",
            "Machine learning is a subset of artificial intelligence."
        ],
        "doc2_dl.txt": [
            "Deep learning uses neural networks.",
            "Neural networks have many layers."
        ],
        "doc3_sports.txt": [
            "Football is a popular sport.",
            "Teams compete to score goals."
        ]
    }

    qa = MultiDocumentQA()

    question = "What is machine learning?"
    answer = qa.ask(question, documents)

    print("\nQuestion:", question)
    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()
