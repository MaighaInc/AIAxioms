"""
Safety-Filtered LLM
-------------------
This program demonstrates how
LLM outputs are filtered to ensure
safe and responsible responses.

Author: AI Course
"""

class SafetyFilter:
    def __init__(self):
        self.blocked_keywords = [
            "hate",
            "violence",
            "illegal",
            "harm",
            "kill"
        ]

    def is_safe(self, text):
        text_lower = text.lower()
        for word in self.blocked_keywords:
            if word in text_lower:
                return False
        return True


class SimpleLLM:
    def generate(self, prompt):
        # Simulated generation
        return f"Generated response to: {prompt}"


class SafetyFilteredLLM:
    def __init__(self):
        self.llm = SimpleLLM()
        self.safety_filter = SafetyFilter()

    def respond(self, prompt):
        if not self.safety_filter.is_safe(prompt):
            return "⚠️ This request violates safety guidelines."

        response = self.llm.generate(prompt)

        if not self.safety_filter.is_safe(response):
            return "⚠️ Generated content blocked for safety reasons."

        return response


def main():
    print("SAFETY-FILTERED LLM")
    print("--------------------")

    model = SafetyFilteredLLM()

    prompts = [
        "Explain generative AI",
        "How to cause harm using AI"
    ]

    for prompt in prompts:
        print("\nUser:", prompt)
        print("LLM:", model.respond(prompt))


if __name__ == "__main__":
    main()
