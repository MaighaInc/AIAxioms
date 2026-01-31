"""
Memory Decay and Reinforcement
-----------------------------
This program demonstrates how
AI memory decays over time
and is reinforced when reused.

Author: AI Course
"""

import time


class MemoryItem:
    def __init__(self, content):
        self.content = content
        self.strength = 1.0
        self.last_accessed = time.time()

    def reinforce(self):
        self.strength += 0.5
        self.last_accessed = time.time()

    def decay(self, decay_rate=0.1):
        time_passed = time.time() - self.last_accessed
        self.strength -= decay_rate * time_passed
        self.strength = max(self.strength, 0)


class MemorySystem:
    def __init__(self):
        self.memories = []

    def add_memory(self, content):
        self.memories.append(MemoryItem(content))

    def access_memory(self, content):
        for mem in self.memories:
            if mem.content == content:
                mem.reinforce()
                return mem
        return None

    def decay_all(self):
        for mem in self.memories:
            mem.decay()

    def cleanup(self, threshold=0.3):
        self.memories = [
            mem for mem in self.memories
            if mem.strength >= threshold
        ]


def main():
    print("MEMORY DECAY & REINFORCEMENT")
    print("----------------------------")

    system = MemorySystem()

    system.add_memory("User prefers Python.")
    system.add_memory("User asked about neural networks.")
    system.add_memory("User likes concise explanations.")

    print("\nInitial Memories:")
    for mem in system.memories:
        print(mem.content, "| Strength:", round(mem.strength, 2))

    time.sleep(1)
    system.decay_all()

    system.access_memory("User prefers Python.")

    system.cleanup()

    print("\nUpdated Memories:")
    for mem in system.memories:
        print(mem.content, "| Strength:", round(mem.strength, 2))


if __name__ == "__main__":
    main()
