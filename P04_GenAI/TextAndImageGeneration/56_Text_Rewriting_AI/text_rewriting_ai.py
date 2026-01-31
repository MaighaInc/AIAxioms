"""
Text Rewriting AI
-----------------
This program rewrites text by applying
controlled transformation rules.

Author: AI Course
"""

class TextRewriter:
    def __init__(self):
        self.rewrite_rules = {
            "good": "excellent",
            "bad": "poor",
            "big": "large",
            "small": "tiny",
            "fast": "quick",
            "slow": "gradual"
        }

    def rewrite(self, text):
        words = text.split()
        rewritten = []

        for word in words:
            clean_word = word.lower().strip(".,")
            if clean_word in self.rewrite_rules:
                rewritten.append(self.rewrite_rules[clean_word])
            else:
                rewritten.append(word)

        return " ".join(rewritten)


def main():
    print("TEXT REWRITING AI")
    print("------------------")

    text = "The product is good and fast but the delivery was slow."
    rewriter = TextRewriter()

    rewritten_text = rewriter.rewrite(text)

    print("\nOriginal Text:")
    print(text)

    print("\nRewritten Text:")
    print(rewritten_text)


if __name__ == "__main__":
    main()
