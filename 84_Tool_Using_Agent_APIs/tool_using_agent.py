"""
Tool-Using AI Agent
-------------------
This program demonstrates an AI agent
that decides when to call tools (APIs)
to complete tasks.

Author: AI Course
"""

class CalculatorAPI:
    def run(self, expression):
        try:
            return eval(expression)
        except Exception:
            return "Invalid expression"


class WeatherAPI:
    def run(self, city):
        # Simulated API response
        return f"The weather in {city} is sunny."


class ToolUsingAgent:
    def __init__(self):
        self.tools = {
            "calculator": CalculatorAPI(),
            "weather": WeatherAPI()
        }

    def perceive(self, task):
        return task.lower()

    def decide_and_act(self, task):
        if "calculate" in task:
            expression = task.replace("calculate", "").strip()
            return self.tools["calculator"].run(expression)

        if "weather" in task:
            city = task.replace("weather", "").strip()
            return self.tools["weather"].run(city)

        return "No suitable tool found. Responding with reasoning."

    def run(self, task):
        print("Agent received task:", task)
        interpreted = self.perceive(task)
        result = self.decide_and_act(interpreted)
        print("Agent result:", result)


def main():
    print("TOOL-USING AI AGENT")
    print("--------------------")

    agent = ToolUsingAgent()

    tasks = [
        "Calculate 15 * 4",
        "Weather Bangalore",
        "Explain machine learning"
    ]

    for task in tasks:
        print()
        agent.run(task)


if __name__ == "__main__":
    main()
