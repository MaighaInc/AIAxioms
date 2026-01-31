"""
RAG Chatbot Over Documents
--------------------------
This program answers questions using
retrieved document chunks.

Author: AI Course
"""

import math
from collections import Counter


class SimpleEmbedder:
    def tokenize(self, text):
        return text.lower().split()

    def embed(self, text, vocab):
        counts = Counter(self.tokenize(text))
        return [counts[word] for word in vocab]


class RAGChatbot:
    def cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        if mag1 == 0 or mag2 == 0:
            return 0
        return dot / (mag1 * mag2)

    def retrieve(self, query, chunks):
        embedder = SimpleEmbedder()
        vocab = set()
        for chunk in chunks:
            vocab.update(embedder.tokenize(chunk))
        vocab.update(embedder.tokenize(query))
        vocab = list(vocab)

        query_vec = embedder.embed(query, vocab)

        scored_chunks = []
        for chunk in chunks:
            chunk_vec = embedder.embed(chunk, vocab)
            score = self.cosine_similarity(query_vec, chunk_vec)
            scored_chunks.append((chunk, score))

        scored_chunks.sort(key=lambda x: x[1], reverse=True)
        return scored_chunks[:2]

    def generate_answer(self, question, retrieved_chunks):
        context = " ".join(chunk for chunk, _ in retrieved_chunks)
        return f"Answer based on documents:\n{context}"

    def ask(self, question, chunks):
        retrieved = self.retrieve(question, chunks)
        return self.generate_answer(question, retrieved)


def main():
    print("RAG CHATBOT OVER DOCUMENTS")
    print("---------------------------")

    document_chunks = [
        "Artificial intelligence enables machines to learn from data.",
        "Machine learning is a subset of artificial intelligence.",
        "Deep learning uses neural networks with many layers.",
        "Football is a popular sport played worldwide."
    ]

    chatbot = RAGChatbot()

    question = "What is machine learning?"
    answer = chatbot.ask(question, document_chunks)

    print("\nQuestion:", question)
    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()
