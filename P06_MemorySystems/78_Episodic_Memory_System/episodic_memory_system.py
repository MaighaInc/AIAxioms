"""
Episodic Memory System
---------------------
This program demonstrates how
AI systems store and retrieve
event-based memories.

Author: AI Course
"""

import math
import time
from collections import Counter


class EpisodicMemory:
    def __init__(self):
        self.episodes = []

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

    def store_event(self, description):
        event = {
            "description": description,
            "timestamp": time.time()
        }
        self.episodes.append(event)

    def recall(self, query, top_k=2):
        vocab = set()
        for ep in self.episodes:
            vocab.update(self.tokenize(ep["description"]))
        vocab.update(self.tokenize(query))
        vocab = list(vocab)

        query_vec = self.embed(self.tokenize(query), vocab)

        scored = []
        for ep in self.episodes:
            ep_vec = self.embed(self.tokenize(ep["description"]), vocab)
            score = self.cosine_similarity(query_vec, ep_vec)
            scored.append((ep, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]


def main():
    print("EPISODIC MEMORY SYSTEM")
    print("-----------------------")

    memory = EpisodicMemory()

    memory.store_event("User asked about machine learning basics.")
    memory.store_event("User completed the RAG module.")
    memory.store_event("User requested memory system explanations.")

    query = "What did the user ask earlier?"
    events = memory.recall(query)

    print("\nQuery:", query)
    print("\nRecalled Events:")
    for ep, score in events:
        print(f"Score: {round(score, 3)} | Event: {ep['description']}")


if __name__ == "__main__":
    main()
