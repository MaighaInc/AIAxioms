"""
Streaming RAG Responses
-----------------------
This program demonstrates how RAG
answers can be streamed incrementally.

Author: AI Course
"""

import time
import math
from collections import Counter


class StreamingRAG:
    def tokenize(self, text):
        return text.lower().split()

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

    def retrieve(self, query, documents, top_k=2):
        vocab = set(self.tokenize(query))
        for doc in documents:
            vocab.update(self.tokenize(doc["text"]))
        vocab = list(vocab)

        query_vec = self.embed(self.tokenize(query), vocab)

        scored = []
        for doc in documents:
            doc_vec = self.embed(self.tokenize(doc["text"]), vocab)
            score = self.cosine_similarity(query_vec, doc_vec)
            scored.append((doc, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def stream_answer(self, question, documents):
        retrieved = self.retrieve(question, documents)
        full_text = " ".join(doc["text"] for doc, _ in retrieved)

        print("Answer (streaming):")
        for word in full_text.split():
            print(word, end=" ", flush=True)
            time.sleep(0.2)
        print()


def main():
    print("STREAMING RAG RESPONSES")
    print("-----------------------")

    documents = [
        {"text": "Machine learning is a subset of artificial intelligence."},
        {"text": "Artificial intelligence enables machines to learn."},
        {"text": "Football is a popular sport."}
    ]

    rag = StreamingRAG()

    question = "What is machine learning?"
    print("\nQuestion:", question)
    rag.stream_answer(question, documents)


if __name__ == "__main__":
    main()
