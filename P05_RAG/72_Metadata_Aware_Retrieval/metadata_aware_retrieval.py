"""
Metadata-Aware Retrieval
------------------------
This program demonstrates how
document metadata is used to
filter retrieval results.

Author: AI Course
"""

import math
from collections import Counter


class MetadataAwareRetriever:
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

    def search(self, query, documents, filters=None, top_k=3):
        """
        documents = list of dicts:
        {
          "text": "...",
          "metadata": {"department": "hr", "year": 2024}
        }
        """
        filters = filters or {}

        # Apply metadata filtering
        filtered_docs = []
        for doc in documents:
            allowed = True
            for key, value in filters.items():
                if doc["metadata"].get(key) != value:
                    allowed = False
            if allowed:
                filtered_docs.append(doc)

        # Build vocabulary
        vocab = set(self.tokenize(query))
        for doc in filtered_docs:
            vocab.update(self.tokenize(doc["text"]))
        vocab = list(vocab)

        query_vec = self.embed(self.tokenize(query), vocab)

        scored = []
        for doc in filtered_docs:
            doc_vec = self.embed(self.tokenize(doc["text"]), vocab)
            score = self.cosine_similarity(query_vec, doc_vec)
            scored.append((doc, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]


def main():
    print("METADATA-AWARE RETRIEVAL")
    print("-------------------------")

    documents = [
        {
            "text": "Employee benefits include health insurance.",
            "metadata": {"department": "hr", "year": 2024}
        },
        {
            "text": "Quarterly revenue increased by 20 percent.",
            "metadata": {"department": "finance", "year": 2024}
        },
        {
            "text": "Hiring process includes technical interviews.",
            "metadata": {"department": "hr", "year": 2023}
        }
    ]

    retriever = MetadataAwareRetriever()

    query = "employee benefits"
    filters = {"department": "hr"}

    results = retriever.search(query, documents, filters)

    print("\nQuery:", query)
    print("Filters:", filters)
    print("\nRetrieved Documents:")
    for doc, score in results:
        print(f"Score: {round(score, 3)} | Text: {doc['text']}")


if __name__ == "__main__":
    main()
