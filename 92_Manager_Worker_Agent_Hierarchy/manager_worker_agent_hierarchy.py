"""
Manager–Worker Agent Hierarchy
------------------------------
This program demonstrates how
a manager agent delegates tasks
to worker agents.

Author: AI Course
"""

class WorkerAgent:
    def __init__(self, name):
        self.name = name

    def execute(self, task):
        return f"{self.name} completed task: {task}"


class ManagerAgent:
    def __init__(self):
        self.workers = [
            WorkerAgent("Worker-1"),
            WorkerAgent("Worker-2")
        ]

    def plan_tasks(self, goal):
        return [
            "Research topic",
            "Write summary"
        ]

    def run(self, goal):
        print("Manager received goal:", goal)
        tasks = self.plan_tasks(goal)

        for task, worker in zip(tasks, self.workers):
            result = worker.execute(task)
            print(result)

        print("Manager: All tasks completed")


def main():
    print("MANAGER–WORKER AGENT HIERARCHY")
    print("-------------------------------")

    manager = ManagerAgent()
    manager.run("Explain machine learning")


if __name__ == "__main__":
    main()
