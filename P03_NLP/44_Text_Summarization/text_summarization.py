"""
Text Summarization (From Scratch)
--------------------------------
This program creates a short summary
by selecting the most important sentences.

Author: AI Course
"""

import math
from collections import Counter


class TextSummarizer:
    def tokenize_sentences(self, text):
        return [s.strip() for s in text.split(".") if s.strip()]

    def tokenize_words(self, sentence):
        return sentence.lower().split()

    def summarize(self, text, num_sentences=2):
        sentences = self.tokenize_sentences(text)

        # Calculate word frequencies
        word_freq = Counter()
        for sentence in sentences:
            word_freq.update(self.tokenize_words(sentence))

        # Score sentences
        sentence_scores = {}
        for sentence in sentences:
            words = self.tokenize_words(sentence)
            score = sum(word_freq[word] for word in words)
            sentence_scores[sentence] = score

        # Select top sentences
        ranked = sorted(
            sentence_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        summary = [sentence for sentence, _ in ranked[:num_sentences]]
        return ". ".join(summary) + "."


def main():
    print("TEXT SUMMARIZATION SYSTEM")
    print("--------------------------")

    text = (
        "Natural language processing is a field of artificial intelligence. "
        "It focuses on the interaction between computers and humans. "
        "Text summarization is an important task in NLP. "
        "It helps reduce long documents into shorter versions. "
        "Summarization saves time and improves readability."
    )

    summarizer = TextSummarizer()
    summary = summarizer.summarize(text)

    print("\nOriginal Text:")
    print(text)

    print("\nSummary:")
    print(summary)


if __name__ == "__main__":
    main()
