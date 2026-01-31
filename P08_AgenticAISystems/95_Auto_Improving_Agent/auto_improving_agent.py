"""
Auto-Improving AI Agent
----------------------
This program demonstrates an AI agent
that improves its responses over time
based on feedback from past runs.

Author: AI Course
"""

class AutoImprovingAgent:
    def __init__(self):
        self.knowledge = []
        self.improvement_level = 1

    def generate(self, task):
        return f"Level {self.improvement_level} answer for {task}."

    def evaluate(self, answer):
        print("Evaluating answer...")
        # Simulated feedback
        if self.improvement_level < 3:
            return "Needs more detail"
        return "Good quality"

    def learn(self, feedback):
        if "Needs more detail" in feedback:
            self.improvement_level += 1
            self.knowledge.append("Add more explanation")

    def run(self, task):
        print("Task:", task)

        answer = self.generate(task)
        print("Generated:", answer)

        feedback = self.evaluate(answer)
        print("Feedback:", feedback)

        self.learn(feedback)
        print("Updated Improvement Level:", self.improvement_level)


def main():
    print("AUTO-IMPROVING AI AGENT")
    print("-----------------------")

    agent = AutoImprovingAgent()

    for i in range(3):
        print(f"\n--- Iteration {i + 1} ---")
        agent.run("Explain reinforcement learning")


if __name__ == "__main__":
    main()
