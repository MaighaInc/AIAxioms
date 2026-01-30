"""
POS Tagger from Scratch
-----------------------
This program assigns Part-of-Speech tags
to words using simple rules and statistics.

Author: AI Course
"""

from collections import defaultdict


class POSTagger:
    def __init__(self):
        # word -> tag -> count
        self.word_tag_counts = defaultdict(lambda: defaultdict(int))
        self.tag_counts = defaultdict(int)

    def train(self, tagged_sentences):
        """
        tagged_sentences: list of lists like
        [("I","PRON"), ("love","VERB"), ("NLP","NOUN")]
        """
        for sentence in tagged_sentences:
            for word, tag in sentence:
                word = word.lower()
                self.word_tag_counts[word][tag] += 1
                self.tag_counts[tag] += 1

    def predict(self, sentence):
        """
        sentence: list of words
        """
        predictions = []
        for word in sentence:
            word_l = word.lower()
            if word_l in self.word_tag_counts:
                # choose most frequent tag for this word
                tag = max(
                    self.word_tag_counts[word_l],
                    key=self.word_tag_counts[word_l].get
                )
            else:
                # simple fallback rule
                if word_l.endswith("ing"):
                    tag = "VERB"
                elif word_l.endswith("ly"):
                    tag = "ADV"
                elif word_l.endswith("s"):
                    tag = "NOUN"
                else:
                    tag = "NOUN"
            predictions.append((word, tag))
        return predictions


def main():
    print("POS TAGGER FROM SCRATCH")
    print("------------------------")

    # Training data
    training_data = [
        [("I", "PRON"), ("love", "VERB"), ("NLP", "NOUN")],
        [("NLP", "NOUN"), ("is", "VERB"), ("fun", "ADJ")],
        [("She", "PRON"), ("is", "VERB"), ("learning", "VERB")],
        [("He", "PRON"), ("runs", "VERB"), ("fast", "ADV")]
    ]

    tagger = POSTagger()
    tagger.train(training_data)

    test_sentence = ["I", "am", "learning", "nlp"]
    result = tagger.predict(test_sentence)

    print("\nSentence:")
    print(test_sentence)

    print("\nPOS Tags:")
    for word, tag in result:
        print(f"{word} -> {tag}")


if __name__ == "__main__":
    main()
