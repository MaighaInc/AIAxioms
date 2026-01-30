"""
Hybrid Chatbot (Rule + ML Style)
--------------------------------
This chatbot combines rule-based logic
with text similarity to generate responses.

Author: AI Course
"""

import math
from collections import Counter


class HybridChatbot:
    def __init__(self):
        # Rule-based responses
        self.rules = {
            "hello": "Hello! How can I help you?",
            "hi": "Hi there! What can I do for you?",
            "bye": "Goodbye! Have a great day.",
            "thanks": "You're welcome!"
        }

        # Knowledge base for ML-style matching
        self.knowledge = {
            "what is nlp": "NLP stands for Natural Language Processing.",
            "what is machine learning": "Machine learning allows systems to learn from data.",
            "what is ai": "AI stands for Artificial Intelligence."
        }

    def tokenize(self, text):
        return text.lower().split()

    def vectorize(self, text):
        return Counter(self.tokenize(text))

    def cosine_similarity(self, v1, v2):
        common = set(v1.keys()) & set(v2.keys())
        numerator = sum(v1[w] * v2[w] for w in common)

        mag1 = math.sqrt(sum(v ** 2 for v in v1.values()))
        mag2 = math.sqrt(sum(v ** 2 for v in v2.values()))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return numerator / (mag1 * mag2)

    def ml_response(self, user_input):
        user_vec = self.vectorize(user_input)
        best_score = 0
        best_response = None

        for question, answer in self.knowledge.items():
            q_vec = self.vectorize(question)
            score = self.cosine_similarity(user_vec, q_vec)

            if score > best_score:
                best_score = score
                best_response = answer

        if best_score > 0.2:
            return best_response

        return "Sorry, I didn't understand that."

    def respond(self, user_input):
        clean_input = user_input.lower()

        # Rule-based response
        for rule in self.rules:
            if rule in clean_input:
                return self.rules[rule]

        # ML-style response
        return self.ml_response(user_input)


def main():
    print("HYBRID CHATBOT")
    print("---------------")
    print("Type 'bye' to exit.\n")

    bot = HybridChatbot()

    while True:
        user_input = input("You: ")

        response = bot.respond(user_input)
        print("Bot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
