"""
TF-IDF Text Classifier (From Scratch)
------------------------------------
This program implements TF-IDF weighting
and uses it for text classification.

Author: AI Course
"""

import math
from collections import Counter


class TFIDFClassifier:
    def __init__(self):
        self.vocabulary = []
        self.idf = {}
        self.class_word_weights = {}
        self.class_counts = {}

    def tokenize(self, text):
        return text.lower().split()

    def build_vocabulary(self, texts):
        vocab = set()
        for text in texts:
            vocab.update(self.tokenize(text))
        self.vocabulary = list(vocab)

    def compute_idf(self, texts):
        total_docs = len(texts)
        for word in self.vocabulary:
            doc_count = sum(
                1 for text in texts if word in self.tokenize(text)
            )
            self.idf[word] = math.log((total_docs + 1) / (doc_count + 1)) + 1

    def tfidf_vector(self, text):
        tokens = self.tokenize(text)
        tf = Counter(tokens)
        vector = {
            word: tf[word] * self.idf.get(word, 0)
            for word in tf
        }
        return vector

    def train(self, texts, labels):
        self.build_vocabulary(texts)
        self.compute_idf(texts)

        for text, label in zip(texts, labels):
            if label not in self.class_word_weights:
                self.class_word_weights[label] = Counter()
                self.class_counts[label] = 0

            self.class_counts[label] += 1
            tfidf = self.tfidf_vector(text)
            self.class_word_weights[label].update(tfidf)

    def predict(self, text):
        tfidf = self.tfidf_vector(text)
        scores = {}

        for label in self.class_word_weights:
            score = 0
            for word, value in tfidf.items():
                score += self.class_word_weights[label].get(word, 0) * value
            scores[label] = score

        return max(scores, key=scores.get)


def main():
    print("TF-IDF TEXT CLASSIFIER")
    print("----------------------")

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

    classifier = TFIDFClassifier()
    classifier.train(texts, labels)

    test_text = "win money offer"
    prediction = classifier.predict(test_text)

    print("\nTest Text:", test_text)
    print("Predicted Class:", prediction)


if __name__ == "__main__":
    main()
