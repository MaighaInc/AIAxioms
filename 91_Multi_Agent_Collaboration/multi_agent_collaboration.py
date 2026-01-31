"""
Multi-Agent Collaboration
-------------------------
This program demonstrates how
multiple AI agents collaborate
to solve a task together.

Author: AI Course
"""

class ResearchAgent:
    def work(self, topic):
        return f"ResearchAgent: Collected info on {topic}."


class WritingAgent:
    def work(self, content):
        return f"WritingAgent: Wrote summary using '{content}'."


class CoordinatorAgent:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()

    def run(self, topic):
        print("Coordinator: Starting collaboration")

        research_output = self.research_agent.work(topic)
        print(research_output)

        writing_output = self.writing_agent.work(research_output)
        print(writing_output)

        print("Coordinator: Task completed")


def main():
    print("MULTI-AGENT COLLABORATION")
    print("-------------------------")

    coordinator = CoordinatorAgent()
    coordinator.run("machine learning")


if __name__ == "__main__":
    main()
