"""
Document Clustering (From Scratch)
----------------------------------
This program groups documents based on
text similarity using simple K-means logic.

Author: AI Course
"""

import math
import random
from collections import Counter


class DocumentClustering:
    def tokenize(self, text):
        return text.lower().split()

    def vectorize(self, text, vocabulary):
        tokens = self.tokenize(text)
        counts = Counter(tokens)
        return [counts.get(word, 0) for word in vocabulary]

    def cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        if mag1 == 0 or mag2 == 0:
            return 0
        return dot / (mag1 * mag2)

    def average_vector(self, vectors):
        return [
            sum(values) / len(values)
            for values in zip(*vectors)
        ]

    def cluster(self, documents, k=2, iterations=5):
        # Build vocabulary
        vocab = set()
        for doc in documents:
            vocab.update(self.tokenize(doc))
        vocab = list(vocab)

        vectors = [self.vectorize(doc, vocab) for doc in documents]

        # Initialize centroids randomly
        centroids = random.sample(vectors, k)

        for _ in range(iterations):
            clusters = [[] for _ in range(k)]

            for vec in vectors:
                similarities = [
                    self.cosine_similarity(vec, c)
                    for c in centroids
                ]
                cluster_id = similarities.index(max(similarities))
                clusters[cluster_id].append(vec)

            # Update centroids
            for i in range(k):
                if clusters[i]:
                    centroids[i] = self.average_vector(clusters[i])

        return clusters, centroids


def main():
    print("DOCUMENT CLUSTERING")
    print("--------------------")

    documents = [
        "machine learning improves models",
        "deep learning uses neural networks",
        "artificial intelligence and machine learning",
        "football match and sports news",
        "sports teams and football players",
        "latest sports updates"
    ]

    clustering = DocumentClustering()
    clusters, _ = clustering.cluster(documents, k=2)

    print("\nDocuments grouped into clusters:")
    for i, cluster in enumerate(clusters):
        print(f"\nCluster {i + 1}:")
        for doc in cluster:
            print(doc)


if __name__ == "__main__":
    main()
