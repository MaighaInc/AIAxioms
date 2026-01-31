"""
Planning Agent using ReAct Pattern
---------------------------------
This program demonstrates a planning
agent that reasons step-by-step,
uses tools, and observes results.

Author: AI Course
"""

class SearchTool:
    def run(self, query):
        return f"Search result for '{query}': Machine learning is a subset of AI."


class CalculatorTool:
    def run(self, expression):
        return eval(expression)


class ReActAgent:
    def __init__(self):
        self.search_tool = SearchTool()
        self.calculator_tool = CalculatorTool()

    def think(self, task):
        if "calculate" in task:
            return "I need to calculate a value."
        if "what is" in task:
            return "I should search for information."
        return "I can answer directly."

    def act(self, thought, task):
        if "calculate" in thought:
            expression = task.replace("calculate", "").strip()
            return self.calculator_tool.run(expression)
        if "search" in thought:
            query = task.replace("what is", "").strip()
            return self.search_tool.run(query)
        return "Direct answer generated."

    def run(self, task):
        print("Task:", task)

        thought = self.think(task.lower())
        print("Thought:", thought)

        observation = self.act(thought, task.lower())
        print("Observation:", observation)

        print("Final Answer:", observation)


def main():
    print("PLANNING AGENT (ReAct)")
    print("----------------------")

    agent = ReActAgent()

    tasks = [
        "What is machine learning?",
        "Calculate 12 * 8"
    ]

    for task in tasks:
        print()
        agent.run(task)


if __name__ == "__main__":
    main()
