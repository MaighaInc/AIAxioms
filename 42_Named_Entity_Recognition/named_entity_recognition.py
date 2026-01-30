"""
Named Entity Recognition (NER) from Scratch
-------------------------------------------
This program identifies named entities
such as PERSON, LOCATION, and ORGANIZATION.

Author: AI Course
"""

class NER:
    def __init__(self):
        self.person_names = {"john", "mary", "alice"}
        self.locations = {"india", "london", "paris"}
        self.organizations = {"google", "microsoft", "openai"}

    def recognize(self, sentence):
        entities = []
        words = sentence.split()

        for word in words:
            clean_word = word.lower().strip(".,")
            if clean_word in self.person_names:
                entities.append((word, "PERSON"))
            elif clean_word in self.locations:
                entities.append((word, "LOCATION"))
            elif clean_word in self.organizations:
                entities.append((word, "ORGANIZATION"))
            else:
                entities.append((word, "O"))  # Outside entity

        return entities


def main():
    print("NAMED ENTITY RECOGNITION")
    print("-------------------------")

    sentence = "John works at OpenAI in India"

    ner = NER()
    result = ner.recognize(sentence)

    print("\nSentence:")
    print(sentence)

    print("\nRecognized Entities:")
    for word, tag in result:
        print(f"{word} -> {tag}")


if __name__ == "__main__":
    main()
