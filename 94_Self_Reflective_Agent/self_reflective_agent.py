"""
Self-Reflective AI Agent
-----------------------
This program demonstrates an AI agent
that reviews its own output and improves it.

Author: AI Course
"""

class SelfReflectiveAgent:
    def generate(self, question):
        return f"Initial answer: {question} is important in modern AI."

    def reflect(self, answer):
        print("Reflecting on answer...")
        if "important" in answer:
            return "The answer is too vague."
        return "Answer looks specific."

    def improve(self, answer, critique):
        if "vague" in critique:
            return answer + " It improves automation, accuracy, and scalability."
        return answer

    def run(self, question):
        print("Question:", question)

        answer = self.generate(question)
        print(answer)

        critique = self.reflect(answer)
        print("Critique:", critique)

        improved = self.improve(answer, critique)
        print("Improved Answer:", improved)


def main():
    print("SELF-REFLECTIVE AI AGENT")
    print("-------------------------")

    agent = SelfReflectiveAgent()
    agent.run("Machine learning")


if __name__ == "__main__":
    main()
