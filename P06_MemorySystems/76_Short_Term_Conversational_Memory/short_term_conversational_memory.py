"""
Short-Term Conversational Memory
--------------------------------
This program demonstrates how
a chatbot remembers recent messages
within a conversation window.

Author: AI Course
"""

from collections import deque


class ShortTermMemory:
    def __init__(self, max_turns=5):
        self.memory = deque(maxlen=max_turns)

    def add(self, role, message):
        self.memory.append({"role": role, "message": message})

    def get_context(self):
        context = ""
        for item in self.memory:
            context += f"{item['role'].upper()}: {item['message']}\n"
        return context.strip()


class Chatbot:
    def __init__(self):
        self.memory = ShortTermMemory(max_turns=4)

    def respond(self, user_message):
        self.memory.add("user", user_message)

        context = self.memory.get_context()
        response = f"I remember this conversation:\n{context}"

        self.memory.add("assistant", response)
        return response


def main():
    print("SHORT-TERM CONVERSATIONAL MEMORY")
    print("--------------------------------")

    bot = Chatbot()

    messages = [
        "Hello",
        "What is AI?",
        "Explain machine learning",
        "What did I ask earlier?"
    ]

    for msg in messages:
        print("\nUser:", msg)
        reply = bot.respond(msg)
        print("Bot:", reply)


if __name__ == "__main__":
    main()
