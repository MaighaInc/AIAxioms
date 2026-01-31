"""
Markov Chain Text Generator
---------------------------
This program generates text using
a Markov Chain based on word transitions.

Author: AI Course
"""

import random
from collections import defaultdict


class MarkovChainTextGenerator:
    def __init__(self):
        self.model = defaultdict(list)

    def train(self, text):
        words = text.lower().split()
        for i in range(len(words) - 1):
            self.model[words[i]].append(words[i + 1])

    def generate(self, start_word, length=20):
        current = start_word.lower()
        result = [current]

        for _ in range(length - 1):
            next_words = self.model.get(current)
            if not next_words:
                break
            current = random.choice(next_words)
            result.append(current)

        return " ".join(result)


def main():
    print("MARKOV CHAIN TEXT GENERATOR")
    print("----------------------------")

    training_text = (
        "artificial intelligence is powerful "
        "artificial intelligence is transforming technology "
        "technology is evolving rapidly"
    )

    generator = MarkovChainTextGenerator()
    generator.train(training_text)

    generated_text = generator.generate("artificial", length=15)

    print("\nGenerated Text:")
    print(generated_text)


if __name__ == "__main__":
    main()
