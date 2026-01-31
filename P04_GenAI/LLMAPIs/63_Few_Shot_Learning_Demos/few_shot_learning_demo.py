"""
Few-Shot Learning Demo
---------------------
This program demonstrates how
language models learn tasks
from examples inside the prompt.

Author: AI Course
"""

class FewShotModel:
    def generate(self, prompt):
        """
        Simulated LLM behavior.
        """
        if "Positive" in prompt and "Negative" in prompt:
            return "Sentiment: Positive"
        return "Unable to classify"


def main():
    print("FEW-SHOT LEARNING DEMO")
    print("-----------------------")

    llm = FewShotModel()

    prompt = """
Text: I love this product
Sentiment: Positive

Text: This is terrible
Sentiment: Negative

Text: The experience was amazing
Sentiment:
"""

    print("Prompt Sent to Model:")
    print(prompt)

    response = llm.generate(prompt)

    print("\nModel Output:")
    print(response)


if __name__ == "__main__":
    main()
