"""
OpenAI-Compatible LLM Wrapper
-----------------------------
This module provides a clean interface
for interacting with any LLM API.

Author: AI Course
"""

class LLMWrapper:
    def __init__(self, model_name="gpt-like-model"):
        self.model_name = model_name

    def generate(self, prompt, max_tokens=100, temperature=0.7):
        """
        Simulated LLM API call.
        Replace this with real API logic later.
        """
        return (
            f"[Model: {self.model_name}]\n"
            f"Response to prompt:\n"
            f"'{prompt}'\n\n"
            f"(Generated with temperature={temperature}, "
            f"max_tokens={max_tokens})"
        )


def main():
    print("OPENAI-COMPATIBLE LLM WRAPPER")
    print("-----------------------------")

    llm = LLMWrapper(model_name="mini-gpt")

    prompt = "Explain generative AI in simple terms"
    response = llm.generate(prompt, max_tokens=60, temperature=0.5)

    print("\nPrompt:")
    print(prompt)

    print("\nLLM Response:")
    print(response)


if __name__ == "__main__":
    main()
