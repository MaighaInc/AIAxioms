"""
Tool-Using LLM
--------------
This program demonstrates how an LLM
decides when to call an external tool
and uses the result to respond.

Author: AI Course
"""

class CalculatorTool:
    def calculate(self, expression):
        try:
            return eval(expression)
        except Exception:
            return "Invalid expression"


class ToolUsingLLM:
    def __init__(self):
        self.calculator = CalculatorTool()

    def respond(self, prompt):
        prompt_lower = prompt.lower()

        if "calculate" in prompt_lower or "math" in prompt_lower:
            expression = prompt_lower.replace("calculate", "").strip()
            result = self.calculator.calculate(expression)
            return f"The result is {result}"

        return "I can answer questions or calculate math problems."


def main():
    print("TOOL-USING LLM")
    print("----------------")

    llm = ToolUsingLLM()

    prompts = [
        "Calculate 25 * 4 + 10",
        "What can you do?"
    ]

    for prompt in prompts:
        print("\nUser:", prompt)
        print("LLM:", llm.respond(prompt))


if __name__ == "__main__":
    main()
