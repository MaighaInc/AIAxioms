"""
Debate-Based Reasoning Agents
----------------------------
This program demonstrates how
multiple agents debate a question
and a judge agent selects the best answer.

Author: AI Course
"""

class ProAgent:
    def argue(self, question):
        return f"ProAgent: {question} is beneficial because it improves efficiency."

class ConAgent:
    def argue(self, question):
        return f"ConAgent: {question} has risks related to misuse and bias."

class JudgeAgent:
    def decide(self, pro_argument, con_argument):
        if "beneficial" in pro_argument:
            return "Judge: Balanced view accepted with caution."
        return "Judge: Insufficient argument."

class DebateSystem:
    def run(self, question):
        pro = ProAgent()
        con = ConAgent()
        judge = JudgeAgent()

        pro_arg = pro.argue(question)
        con_arg = con.argue(question)

        print(pro_arg)
        print(con_arg)

        decision = judge.decide(pro_arg, con_arg)
        print(decision)


def main():
    print("DEBATE-BASED REASONING AGENTS")
    print("-----------------------------")

    debate = DebateSystem()
    debate.run("Using AI in education")


if __name__ == "__main__":
    main()
