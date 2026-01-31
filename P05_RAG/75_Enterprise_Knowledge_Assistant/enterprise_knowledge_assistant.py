"""
Enterprise Knowledge Assistant
------------------------------
This program demonstrates a full
enterprise-ready RAG assistant.

Author: AI Course
"""

import math
import time
from collections import Counter


class EnterpriseRAG:
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

    def retrieve(self, query, documents, filters=None, top_k=2):
        filters = filters or {}

        # Metadata filtering
        allowed_docs = []
        for doc in documents:
            allowed = True
            for k, v in filters.items():
                if doc["metadata"].get(k) != v:
                    allowed = False
            if allowed:
                allowed_docs.append(doc)

        # Build vocab
        vocab = set(self.tokenize(query))
        for doc in allowed_docs:
            vocab.update(self.tokenize(doc["text"]))
        vocab = list(vocab)

        query_vec = self.embed(self.tokenize(query), vocab)

        scored = []
        for doc in allowed_docs:
            doc_vec = self.embed(self.tokenize(doc["text"]), vocab)
            score = self.cosine_similarity(query_vec, doc_vec)
            scored.append((doc, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def stream_answer(self, question, retrieved_docs):
        answer_text = " ".join(doc["text"] for doc, _ in retrieved_docs)

        print("\nAnswer (streaming):")
        for word in answer_text.split():
            print(word, end=" ", flush=True)
            time.sleep(0.15)
        print("\n")

        print("Citations:")
        for i, (doc, _) in enumerate(retrieved_docs, start=1):
            print(f"[{i}] {doc['source']}")


def main():
    print("ENTERPRISE KNOWLEDGE ASSISTANT")
    print("--------------------------------")

    documents = [
        {
            "text": "Employee benefits include health insurance and paid leave.",
            "source": "hr_policy.pdf",
            "metadata": {"department": "hr", "year": 2024}
        },
        {
            "text": "Machine learning improves business decision making.",
            "source": "ai_strategy.pdf",
            "metadata": {"department": "tech", "year": 2024}
        },
        {
            "text": "Quarterly revenue increased by twenty percent.",
            "source": "finance_report.pdf",
            "metadata": {"department": "finance", "year": 2024}
        }
    ]

    assistant = EnterpriseRAG()

    question = "What benefits do employees have?"
    filters = {"department": "hr"}

    print("\nQuestion:", question)
    print("Filters:", filters)

    retrieved = assistant.retrieve(question, documents, filters)
    assistant.stream_answer(question, retrieved)


if __name__ == "__main__":
    main()
