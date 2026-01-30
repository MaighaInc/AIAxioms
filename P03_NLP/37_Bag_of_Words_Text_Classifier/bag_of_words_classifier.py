"""
Bag-of-Words Text Classifier
----------------------------
This program implements a simple
Bag-of-Words model and uses it
to classify text as Spam or Ham.

Author: AI Course
"""

import math
from collections import Counter


class BagOfWordsClassifier:
    def __init__(self):
        self.vocabulary = []
        self.word_counts = {}
        self.class_counts = {}
        self.total_docs = 0

    def tokenize(self, text):
        return text.lower().split()

    def build_vocabulary(self, texts):
        vocab = set()
        for text in texts:
            vocab.update(self.tokenize(text))
        self.vocabulary = list(vocab)

    def vectorize(self, text):
        tokens = self.tokenize(text)
        vector = [tokens.count(word) for word in self.vocabulary]
        return vector

    def train(self, texts, labels):
        self.total_docs = len(texts)
        self.build_vocabulary(texts)

        for label in labels:
            self.class_counts[label] = self.class_counts.get(label, 0) + 1

        for text, label in zip(texts, labels):
            tokens = self.tokenize(text)
            if label not in self.word_counts:
                self.word_counts[label] = Counter()
            self.word_counts[label].update(tokens)

    def predict(self, text):
        tokens = self.tokenize(text)
        scores = {}

        for label in self.class_counts:
            score = math.log(self.class_counts[label] / self.total_docs)

            for word in tokens:
                word_freq = self.word_counts[label].get(word, 0) + 1
                score += math.log(word_freq)

            scores[label] = score

        return max(scores, key=scores.get)


def main():
    print("BAG-OF-WORDS TEXT CLASSIFIER")
    print("-----------------------------")

    texts = [
        "win money now",
        "limited offer win",
        "meeting at office",
        "project discussion tomorrow",
        "win big prizes",
        "office meeting schedule"
    ]

    labels = [
        "Spam",
        "Spam",
        "Ham",
        "Ham",
        "Spam",
        "Ham"
    ]

    classifier = BagOfWordsClassifier()
    classifier.train(texts, labels)

    test_text = "win money offer"
    prediction = classifier.predict(test_text)

    print("\nTest Text:", test_text)
    print("Predicted Class:", prediction)


if __name__ == "__main__":
    main()
