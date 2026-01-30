"""
Text Similarity Engine (From Scratch)
------------------------------------
This program compares two pieces of text
and measures how similar they are.

Author: AI Course
"""

import math
from collections import Counter


class TextSimilarityEngine:
    def tokenize(self, text):
        return text.lower().split()

    def vectorize(self, text):
        tokens = self.tokenize(text)
        return Counter(tokens)

    def cosine_similarity(self, vec1, vec2):
        common = set(vec1.keys()) & set(vec2.keys())
        numerator = sum(vec1[w] * vec2[w] for w in common)

        mag1 = math.sqrt(sum(v ** 2 for v in vec1.values()))
        mag2 = math.sqrt(sum(v ** 2 for v in vec2.values()))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return numerator / (mag1 * mag2)

    def similarity(self, text1, text2):
        v1 = self.vectorize(text1)
        v2 = self.vectorize(text2)
        return self.cosine_similarity(v1, v2)


def main():
    print("TEXT SIMILARITY ENGINE")
    print("-----------------------")

    text_a = "Machine learning is a part of artificial intelligence"
    text_b = "Artificial intelligence includes machine learning techniques"

    engine = TextSimilarityEngine()
    score = engine.similarity(text_a, text_b)

    print("\nText A:")
    print(text_a)

    print("\nText B:")
    print(text_b)

    print("\nSimilarity Score:", round(score, 3))


if __name__ == "__main__":
    main()
