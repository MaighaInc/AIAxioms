"""
Human-in-the-Loop AI System
--------------------------
This program demonstrates how
AI outputs are reviewed and approved
by humans before final action.

Author: AI Course
"""

class AIModel:
    def generate(self, input_text):
        return f"AI suggestion for '{input_text}'"


class HumanReviewer:
    def review(self, ai_output):
        print("AI Output:", ai_output)
        decision = input("Approve this output? (yes/no): ").strip().lower()
        return decision == "yes"


class HITLSystem:
    def __init__(self):
        self.ai = AIModel()
        self.human = HumanReviewer()

    def run(self, task):
        ai_output = self.ai.generate(task)
        approved = self.human.review(ai_output)

        if approved:
            print("✅ Output approved and executed.")
        else:
            print("❌ Output rejected. Human intervention required.")


def main():
    print("HUMAN-IN-THE-LOOP AI SYSTEM")
    print("----------------------------")

    system = HITLSystem()
    system.run("Approve loan application")


if __name__ == "__main__":
    main()
