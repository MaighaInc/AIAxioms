"""
Text Completion Engine
----------------------
This program demonstrates how text
completion works by repeatedly
predicting the next token.

Author: AI Course
"""

import random
from collections import defaultdict


class TextCompletionEngine:
    def __init__(self):
        self.model = defaultdict(list)

    def train(self, text):
        words = text.lower().split()
        for i in range(len(words) - 1):
            self.model[words[i]].append(words[i + 1])

    def complete(self, prompt, max_tokens=10):
        words = prompt.lower().split()
        current = words[-1]
        output = words[:]

        for _ in range(max_tokens):
            next_words = self.model.get(current)
            if not next_words:
                break
            next_word = random.choice(next_words)
            output.append(next_word)
            current = next_word

        return " ".join(output)


def main():
    print("TEXT COMPLETION ENGINE")
    print("-----------------------")

    training_text = (
        "artificial intelligence is transforming the world "
        "language models generate text "
        "text completion predicts the next word"
    )

    engine = TextCompletionEngine()
    engine.train(training_text)

    prompt = "artificial intelligence"
    completed = engine.complete(prompt, max_tokens=8)

    print("\nPrompt:")
    print(prompt)

    print("\nCompleted Text:")
    print(completed)


if __name__ == "__main__":
    main()
