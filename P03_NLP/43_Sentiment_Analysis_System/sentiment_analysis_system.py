"""
Sentiment Analysis System (From Scratch)
----------------------------------------
This program classifies text sentiment
as Positive or Negative using TF-IDF ideas.

Author: AI Course
"""

import math
from collections import Counter


class SentimentAnalyzer:
    def __init__(self):
        self.vocab = set()
        self.word_scores = {"Positive": Counter(), "Negative": Counter()}
        self.class_counts = {"Positive": 0, "Negative": 0}

    def tokenize(self, text):
        return text.lower().split()

    def train(self, texts, labels):
        for text, label in zip(texts, labels):
            self.class_counts[label] += 1
            tokens = self.tokenize(text)
            self.vocab.update(tokens)
            self.word_scores[label].update(tokens)

    def predict(self, text):
        tokens = self.tokenize(text)
        scores = {}

        for label in self.class_counts:
            score = math.log(self.class_counts[label] + 1)
            for word in tokens:
                score += math.log(self.word_scores[label].get(word, 0) + 1)
            scores[label] = score

        return max(scores, key=scores.get)


def main():
    print("SENTIMENT ANALYSIS SYSTEM")
    print("--------------------------")

    texts = [
        "I love this product",
        "This is amazing",
        "Very happy with the service",
        "I hate this experience",
        "This is terrible",
        "Very disappointed and bad"
    ]

    labels = [
        "Positive",
        "Positive",
        "Positive",
        "Negative",
        "Negative",
        "Negative"
    ]

    analyzer = SentimentAnalyzer()
    analyzer.train(texts, labels)

    test_text = "I am very happy"
    prediction = analyzer.predict(test_text)

    print("\nTest Text:", test_text)
    print("Predicted Sentiment:", prediction)


if __name__ == "__main__":
    main()
