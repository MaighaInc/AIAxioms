"""
Prompt Engineering Experiments
------------------------------
This program demonstrates how
different prompts produce
different outputs from the same model.

Author: AI Course
"""

def simple_model(prompt):
    """
    A mock language model to demonstrate
    prompt sensitivity.
    """
    prompt = prompt.lower()

    if "explain" in prompt:
        return "This is a detailed explanation of the topic."
    elif "summarize" in prompt:
        return "This is a short summary."
    elif "steps" in prompt:
        return "Step 1, Step 2, Step 3."
    elif "code" in prompt:
        return "Here is a sample code snippet."
    else:
        return "General response."


def main():
    print("PROMPT ENGINEERING EXPERIMENTS")
    print("-------------------------------")

    prompts = [
        "Explain artificial intelligence",
        "Summarize artificial intelligence",
        "Give steps to learn artificial intelligence",
        "Write code for artificial intelligence"
    ]

    for prompt in prompts:
        print("\nPrompt:", prompt)
        print("Model Output:", simple_model(prompt))


if __name__ == "__main__":
    main()
