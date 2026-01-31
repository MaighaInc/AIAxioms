"""
Multi-Prompt Chain Execution
----------------------------
This program demonstrates how
multiple prompts are executed
in sequence using an LLM wrapper.

Author: AI Course
"""

class MockLLM:
    def generate(self, prompt):
        return f"Response for: {prompt}"


class PromptChain:
    def __init__(self, llm):
        self.llm = llm
        self.steps = []

    def add_step(self, prompt_template):
        self.steps.append(prompt_template)

    def run(self, input_text):
        context = input_text
        for step in self.steps:
            prompt = step.format(context=context)
            context = self.llm.generate(prompt)
        return context


def main():
    print("MULTI-PROMPT CHAIN EXECUTION")
    print("-----------------------------")

    llm = MockLLM()
    chain = PromptChain(llm)

    chain.add_step("Summarize this text: {context}")
    chain.add_step("Extract key points from summary: {context}")
    chain.add_step("Generate a title from key points: {context}")

    input_text = "Generative AI enables machines to create text, images, and code."

    result = chain.run(input_text)

    print("\nFinal Output:")
    print(result)


if __name__ == "__main__":
    main()
