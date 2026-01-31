"""
Code Writing AI Agent
---------------------
This program demonstrates an AI agent
that generates Python code
based on a given task.

Author: AI Course
"""

class CodeWritingAgent:
    def plan(self, task):
        print("Planning code structure...")
        if "sort" in task:
            return "Write a function to sort a list."
        return "Write a generic function."

    def write_code(self, plan):
        if "sort" in plan:
            return '''
def sort_numbers(numbers):
    return sorted(numbers)
'''
        return '''
def example():
    pass
'''

    def run(self, task):
        print("Task:", task)
        plan = self.plan(task)
        print("Plan:", plan)
        code = self.write_code(plan)
        print("Generated Code:")
        print(code)


def main():
    print("CODE-WRITING AI AGENT")
    print("----------------------")

    agent = CodeWritingAgent()
    agent.run("Write code to sort a list of numbers")


if __name__ == "__main__":
    main()
