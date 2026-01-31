"""
Agent with Memory and Tools
---------------------------
This program demonstrates an AI agent
that combines memory, reasoning,
and tool usage.

Author: AI Course
"""

class Memory:
    def __init__(self):
        self.entries = []

    def add(self, text):
        self.entries.append(text)

    def recall(self):
        return self.entries[-3:]


class CalculatorTool:
    def run(self, expression):
        try:
            return eval(expression)
        except:
            return "Calculation error"


class SmartAgent:
    def __init__(self):
        self.memory = Memory()
        self.tools = {
            "calculator": CalculatorTool()
        }

    def think(self, task):
        if "calculate" in task.lower():
            return "use_calculator"
        return "respond"

    def act(self, task):
        decision = self.think(task)

        if decision == "use_calculator":
            expression = task.replace("calculate", "").strip()
            result = self.tools["calculator"].run(expression)
            self.memory.add(f"Calculated {expression} = {result}")
            return result

        response = f"I remember you asked: {self.memory.recall()}"
        self.memory.add(task)
        return response

    def run(self, task):
        print("User:", task)
        output = self.act(task)
        print("Agent:", output)


def main():
    print("AGENT WITH MEMORY + TOOLS")
    print("--------------------------")

    agent = SmartAgent()

    tasks = [
        "Hello",
        "Calculate 10 * 5",
        "What did I ask before?"
    ]

    for task in tasks:
        agent.run(task)
        print()


if __name__ == "__main__":
    main()
