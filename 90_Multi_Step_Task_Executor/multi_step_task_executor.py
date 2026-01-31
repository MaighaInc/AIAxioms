"""
Multi-Step Task Executor
------------------------
This program demonstrates an AI agent
that plans and executes multiple steps
to achieve a complex goal.

Author: AI Course
"""

class MultiStepAgent:
    def plan(self, goal):
        print("Planning steps...")
        if "research" in goal.lower():
            return [
                "Search topic",
                "Summarize findings",
                "Write report"
            ]
        return ["Analyze goal", "Execute task"]

    def execute_step(self, step):
        print(f"Executing step: {step}")
        return f"{step} completed."

    def run(self, goal):
        print("Goal:", goal)
        steps = self.plan(goal)
        results = []

        for step in steps:
            result = self.execute_step(step)
            results.append(result)

        print("\nFinal Results:")
        for res in results:
            print("-", res)


def main():
    print("MULTI-STEP TASK EXECUTOR")
    print("------------------------")

    agent = MultiStepAgent()
    agent.run("Research machine learning trends")


if __name__ == "__main__":
    main()
