"""
Autonomous Research Agent
-------------------------
This program demonstrates an AI agent
that performs autonomous research by
planning, searching, and summarizing.

Author: AI Course
"""

class SearchAPI:
    def run(self, query):
        # Simulated search result
        return f"Result: {query} is a key concept in artificial intelligence."


class AutonomousResearchAgent:
    def __init__(self):
        self.search_api = SearchAPI()

    def plan(self, topic):
        print("Planning research steps...")
        return [
            f"What is {topic}?",
            f"Why is {topic} important?",
            f"Applications of {topic}"
        ]

    def research(self, questions):
        findings = []
        for q in questions:
            print("Searching:", q)
            result = self.search_api.run(q)
            findings.append(result)
        return findings

    def summarize(self, findings):
        print("Summarizing findings...")
        return " ".join(findings)

    def run(self, topic):
        print("Research Topic:", topic)
        questions = self.plan(topic)
        findings = self.research(questions)
        summary = self.summarize(findings)
        print("\nFinal Research Summary:")
        print(summary)


def main():
    print("AUTONOMOUS RESEARCH AGENT")
    print("-------------------------")

    agent = AutonomousResearchAgent()
    agent.run("machine learning")


if __name__ == "__main__":
    main()
