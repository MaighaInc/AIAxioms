"""
Question Answering System (From Scratch)
----------------------------------------
This program answers questions by finding
the most relevant sentence from a passage.

Author: AI Course
"""

from collections import Counter
import math


class QuestionAnsweringSystem:
    def tokenize(self, text):
        return text.lower().split()

    def sentence_similarity(self, question, sentence):
        q_words = self.tokenize(question)
        s_words = self.tokenize(sentence)

        q_vec = Counter(q_words)
        s_vec = Counter(s_words)

        common = set(q_vec.keys()) & set(s_vec.keys())
        numerator = sum(q_vec[w] * s_vec[w] for w in common)

        q_mag = math.sqrt(sum(v ** 2 for v in q_vec.values()))
        s_mag = math.sqrt(sum(v ** 2 for v in s_vec.values()))

        if q_mag == 0 or s_mag == 0:
            return 0

        return numerator / (q_mag * s_mag)

    def answer(self, question, context):
        sentences = [s.strip() for s in context.split(".") if s.strip()]
        scores = {}

        for sentence in sentences:
            scores[sentence] = self.sentence_similarity(question, sentence)

        best_sentence = max(scores, key=scores.get)
        return best_sentence


def main():
    print("QUESTION ANSWERING SYSTEM")
    print("--------------------------")

    context = (
        "Natural language processing is a field of artificial intelligence. "
        "It helps computers understand human language. "
        "Question answering systems allow machines to answer questions. "
        "They are used in search engines and chatbots."
    )

    question = "What does natural language processing do?"

    qa = QuestionAnsweringSystem()
    answer = qa.answer(question, context)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()
