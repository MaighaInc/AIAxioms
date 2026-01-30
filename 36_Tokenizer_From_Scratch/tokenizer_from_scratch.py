"""
Tokenizer from Scratch
----------------------
This program demonstrates how text
is converted into tokens without
using any NLP libraries.

Author: AI Course
"""

import string


class Tokenizer:
    def __init__(self, lowercase=True, remove_punctuation=True):
        self.lowercase = lowercase
        self.remove_punctuation = remove_punctuation

    def tokenize_characters(self, text):
        """
        Character-level tokenization
        """
        return list(text)

    def tokenize_words(self, text):
        """
        Word-level tokenization
        """
        if self.lowercase:
            text = text.lower()

        if self.remove_punctuation:
            text = text.translate(
                str.maketrans("", "", string.punctuation)
            )

        tokens = text.split()
        return tokens

    def tokenize_sentences(self, text):
        """
        Sentence-level tokenization
        """
        sentences = text.replace("!", ".").replace("?", ".")
        return [s.strip() for s in sentences.split(".") if s.strip()]


def main():
    print("TOKENIZER FROM SCRATCH")
    print("-----------------------")

    text = "Hello! Welcome to NLP. Tokenization is the first step."

    tokenizer = Tokenizer()

    print("\nOriginal Text:")
    print(text)

    print("\nCharacter Tokens:")
    print(tokenizer.tokenize_characters(text))

    print("\nWord Tokens:")
    print(tokenizer.tokenize_words(text))

    print("\nSentence Tokens:")
    print(tokenizer.tokenize_sentences(text))


if __name__ == "__main__":
    main()
