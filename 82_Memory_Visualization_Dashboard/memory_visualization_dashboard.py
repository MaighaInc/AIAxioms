"""
Memory Visualization Dashboard
------------------------------
This program visualizes different
types of AI memory in a readable way.

Author: AI Course
"""

import time


class MemoryRecord:
    def __init__(self, memory_type, content, strength=1.0):
        self.memory_type = memory_type
        self.content = content
        self.strength = strength
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


class MemoryDashboard:
    def __init__(self):
        self.memories = []

    def add_memory(self, memory_type, content, strength=1.0):
        self.memories.append(
            MemoryRecord(memory_type, content, strength)
        )

    def display(self):
        print("\n🧠 MEMORY VISUALIZATION DASHBOARD")
        print("=" * 45)

        grouped = {}
        for mem in self.memories:
            grouped.setdefault(mem.memory_type, []).append(mem)

        for mem_type, records in grouped.items():
            print(f"\n🔹 {mem_type.upper()} MEMORY")
            print("-" * 40)
            for rec in records:
                print(
                    f"[{rec.timestamp}] "
                    f"Strength: {round(rec.strength, 2)} | "
                    f"{rec.content}"
                )


def main():
    dashboard = MemoryDashboard()

    dashboard.add_memory(
        "short-term",
        "User asked about machine learning."
    )
    dashboard.add_memory(
        "long-term",
        "User prefers Python examples.",
        strength=1.8
    )
    dashboard.add_memory(
        "episodic",
        "User completed PART 6 – Memory Systems.",
        strength=2.5
    )
    dashboard.add_memory(
        "personalization",
        "Response style set to concise.",
        strength=2.0
    )

    dashboard.display()


if __name__ == "__main__":
    main()
