"""
Topic Modeling using LDA (From Scratch - Conceptual)
----------------------------------------------------
This program demonstrates how documents
can be represented as mixtures of topics.

Author: AI Course
"""

import random
from collections import defaultdict


class SimpleLDA:
    def __init__(self, num_topics):
        self.num_topics = num_topics
        self.word_topic_counts = defaultdict(lambda: defaultdict(int))
        self.topic_counts = defaultdict(int)
        self.doc_topic_counts = []
        self.vocab = set()

    def tokenize(self, text):
        return text.lower().split()

    def train(self, documents, iterations=20):
        tokenized_docs = []
        for doc in documents:
            words = self.tokenize(doc)
            tokenized_docs.append(words)
            self.vocab.update(words)

        # Initialize topic assignments randomly
        topic_assignments = []
        for doc in tokenized_docs:
            doc_topics = []
            for word in doc:
                topic = random.randint(0, self.num_topics - 1)
                doc_topics.append(topic)
                self.word_topic_counts[word][topic] += 1
                self.topic_counts[topic] += 1
            topic_assignments.append(doc_topics)
            self.doc_topic_counts.append(defaultdict(int))
            for t in doc_topics:
                self.doc_topic_counts[-1][t] += 1

        # Gibbs Sampling
        for _ in range(iterations):
            for d, doc in enumerate(tokenized_docs):
                for i, word in enumerate(doc):
                    old_topic = topic_assignments[d][i]

                    # Remove old assignment
                    self.word_topic_counts[word][old_topic] -= 1
                    self.topic_counts[old_topic] -= 1
                    self.doc_topic_counts[d][old_topic] -= 1

                    # Compute probabilities
                    probs = []
                    for t in range(self.num_topics):
                        prob = (
                            (self.word_topic_counts[word][t] + 1) *
                            (self.doc_topic_counts[d][t] + 1)
                        ) / (self.topic_counts[t] + len(self.vocab))
                        probs.append(prob)

                    # Sample new topic
                    new_topic = probs.index(max(probs))

                    topic_assignments[d][i] = new_topic
                    self.word_topic_counts[word][new_topic] += 1
                    self.topic_counts[new_topic] += 1
                    self.doc_topic_counts[d][new_topic] += 1

    def get_topics(self, top_n=3):
        topics = defaultdict(list)
        for word, topic_counts in self.word_topic_counts.items():
            for topic, count in topic_counts.items():
                topics[topic].append((word, count))

        for topic in topics:
            topics[topic] = sorted(
                topics[topic],
                key=lambda x: x[1],
                reverse=True
            )[:top_n]

        return topics


def main():
    print("TOPIC MODELING (LDA)")
    print("---------------------")

    documents = [
        "machine learning improves models",
        "deep learning and neural networks",
        "artificial intelligence and machine learning",
        "football match and sports news",
        "sports teams and football players",
        "latest sports updates"
    ]

    lda = SimpleLDA(num_topics=2)
    lda.train(documents)

    topics = lda.get_topics()

    print("\nDiscovered Topics:")
    for topic, words in topics.items():
        print(f"\nTopic {topic}:")
        for word, count in words:
            print(word, count)


if __name__ == "__main__":
    main()
