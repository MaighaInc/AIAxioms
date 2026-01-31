"""
Single-Task AI Agent
-------------------
This program demonstrates a simple
goal-driven AI agent that performs
one task autonomously.

Author: AI Course
"""

class SingleTaskAgent:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def perceive(self):
        return f"Task received: {self.task}"

    def act(self):
        if not self.completed:
            self.completed = True
            return f"Executing task: {self.task}"
        return "Task already completed."

    def run(self):
        print(self.perceive())
        print(self.act())
        print("Task status:", "DONE" if self.completed else "PENDING")


def main():
    print("SINGLE-TASK AI AGENT")
    print("---------------------")

    agent = SingleTaskAgent("Summarize AI concepts")
    agent.run()


if __name__ == "__main__":
    main()
