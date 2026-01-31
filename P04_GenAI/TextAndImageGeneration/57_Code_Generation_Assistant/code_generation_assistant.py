"""
Code Generation Assistant
-------------------------
This program generates Python code
based on user instructions.

Author: AI Course
"""

class CodeGenerator:
    def generate(self, instruction):
        instruction = instruction.lower()

        if "add two numbers" in instruction:
            return (
                "def add(a, b):\n"
                "    return a + b\n"
            )

        if "factorial" in instruction:
            return (
                "def factorial(n):\n"
                "    if n == 0:\n"
                "        return 1\n"
                "    return n * factorial(n - 1)\n"
            )

        if "fibonacci" in instruction:
            return (
                "def fibonacci(n):\n"
                "    a, b = 0, 1\n"
                "    for _ in range(n):\n"
                "        a, b = b, a + b\n"
                "    return a\n"
            )

        return "# Sorry, I cannot generate code for this instruction."


def main():
    print("CODE GENERATION ASSISTANT")
    print("--------------------------")

    generator = CodeGenerator()

    instructions = [
        "Write a function to add two numbers",
        "Generate Python code for factorial",
        "Create Fibonacci function"
    ]

    for inst in instructions:
        print("\nInstruction:", inst)
        print("Generated Code:\n")
        print(generator.generate(inst))


if __name__ == "__main__":
    main()
