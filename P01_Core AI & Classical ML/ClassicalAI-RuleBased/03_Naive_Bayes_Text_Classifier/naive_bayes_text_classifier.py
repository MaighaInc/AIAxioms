"""
Naive Bayes Text Classifier (From Scratch)
-----------------------------------------
This program classifies text messages as Spam or Ham
using probability-based learning.

Author: AI Course
"""

import math
from collections import defaultdict


class NaiveBayesClassifier:
    def __init__(self):
        self.class_word_counts = defaultdict(lambda: defaultdict(int))
        self.class_counts = defaultdict(int)
        self.vocabulary = set()

    def train(self, data):
        """
        Train the classifier using labeled text data.

        data: list of tuples (text, label)
        """
        for text, label in data:
            self.class_counts[label] += 1
            words = text.lower().split()
            for word in words:
                self.class_word_counts[label][word] += 1
                self.vocabulary.add(word)

    def predict(self, text):
        """
        Predict class label for a given text.
        """
        scores = {}

        for label in self.class_counts:
            # Start with log prior probability
            score = math.log(self.class_counts[label])

            total_words = sum(self.class_word_counts[label].values())
            vocab_size = len(self.vocabulary)

            for word in text.lower().split():
                # Laplace smoothing
                word_count = self.class_word_counts[label].get(word, 0) + 1
                probability = word_count / (total_words + vocab_size)
                score += math.log(probability)

            scores[label] = score

        return max(scores, key=scores.get)


def main():
    print("NAIVE BAYES TEXT CLASSIFIER")
    print("----------------------------")

    # Training data
    training_data = [
        ("Win money now", "Spam"),
        ("Limited offer win big", "Spam"),
        ("Win a free prize", "Spam"),
        ("Meeting tomorrow", "Ham"),
        ("Project discussion", "Ham"),
        ("Let us schedule meeting", "Ham")
    ]

    classifier = NaiveBayesClassifier()
    classifier.train(training_data)

    # Test message
    test_message = "Win free money now"
    prediction = classifier.predict(test_message)

    print("Message:", test_message)
    print("Prediction:", prediction)


if __name__ == "__main__":
    main()
