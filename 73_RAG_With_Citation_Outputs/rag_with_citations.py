"""
RAG with Citation Outputs
------------------------
This program generates answers
along with citations from
retrieved documents.

Author: AI Course
"""

import math
from collections import Counter


class CitationRAG:
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

    def answer(self, question, documents):
        retrieved = self.retrieve(question, documents)
        context = []
        citations = []

        for i, (doc, score) in enumerate(retrieved, start=1):
            context.append(doc["text"])
            citations.append(f"[{i}] {doc['source']}")

        answer = " ".join(context)
        return answer, citations


def main():
    print("RAG WITH CITATION OUTPUTS")
    print("--------------------------")

    documents = [
        {
            "text": "Machine learning is a subset of artificial intelligence.",
            "source": "ml_intro.pdf"
        },
        {
            "text": "Artificial intelligence enables machines to learn from data.",
            "source": "ai_overview.pdf"
        },
        {
            "text": "Football is a popular sport worldwide.",
            "source": "sports.txt"
        }
    ]

    rag = CitationRAG()

    question = "What is machine learning?"
    answer, citations = rag.answer(question, documents)

    print("\nQuestion:", question)
    print("\nAnswer:")
    print(answer)
    print("\nCitations:")
    for cite in citations:
        print(cite)


if __name__ == "__main__":
    main()
