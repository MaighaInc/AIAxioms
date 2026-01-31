"""
Debugging AI Agent
------------------
This program demonstrates an AI agent
that analyzes buggy code, identifies errors,
and suggests fixes.

Author: AI Course
"""

class DebuggingAgent:
    def analyze(self, code):
        print("Analyzing code...")
        if "pritn" in code:
            return "Syntax Error: Did you mean 'print'?"
        if "division by zero" in code:
            return "Runtime Error: Division by zero detected."
        return "No obvious errors found."

    def suggest_fix(self, analysis):
        if "print" in analysis:
            return "Replace 'pritn' with 'print'."
        if "Division by zero" in analysis:
            return "Add a check to prevent division by zero."
        return "Code looks correct."

    def run(self, code):
        print("Original Code:")
        print(code)
        analysis = self.analyze(code)
        print("Analysis:", analysis)
        fix = self.suggest_fix(analysis)
        print("Suggested Fix:", fix)


def main():
    print("DEBUGGING AI AGENT")
    print("------------------")

    buggy_code = """
a = 10
b = 0
pritn(a / b)
"""

    agent = DebuggingAgent()
    agent.run(buggy_code)


if __name__ == "__main__":
    main()
