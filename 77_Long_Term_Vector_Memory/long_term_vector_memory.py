"""
Long-Term Vector Memory
----------------------
This program demonstrates how
AI systems store and retrieve
memories using vector embeddings.

Author: AI Course
"""

import math
from collections import Counter


class VectorMemory:
    def __init__(self):
        self.memories = []

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

    def add_memory(self, text):
        self.memories.append(text)

    def retrieve(self, query, top_k=2):
        vocab = set()
        for mem in self.memories:
            vocab.update(self.tokenize(mem))
        vocab.update(self.tokenize(query))
        vocab = list(vocab)

        query_vec = self.embed(self.tokenize(query), vocab)

        scored = []
        for mem in self.memories:
            mem_vec = self.embed(self.tokenize(mem), vocab)
            score = self.cosine_similarity(query_vec, mem_vec)
            scored.append((mem, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]


def main():
    print("LONG-TERM VECTOR MEMORY")
    print("------------------------")

    memory = VectorMemory()

    memory.add_memory("User likes machine learning topics.")
    memory.add_memory("User asked about neural networks earlier.")
    memory.add_memory("User prefers Python examples.")

    query = "What programming language do I like?"
    results = memory.retrieve(query)

    print("\nQuery:", query)
    print("\nRetrieved Memories:")
    for mem, score in results:
        print(f"Score: {round(score, 3)} | Memory: {mem}")


if __name__ == "__main__":
    main()
