"""
Cross-Session Memory Store
--------------------------
This program demonstrates how
AI memory persists across sessions
using file-based storage.

Author: AI Course
"""

import json
import os


class CrossSessionMemory:
    def __init__(self, filepath="memory_store.json"):
        self.filepath = filepath
        self.memory = self.load()

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                return json.load(f)
        return {}

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.memory, f, indent=2)

    def set(self, key, value):
        self.memory[key] = value
        self.save()

    def get(self, key, default=None):
        return self.memory.get(key, default)


def main():
    print("CROSS-SESSION MEMORY STORE")
    print("---------------------------")

    memory = CrossSessionMemory()

    # Store memory
    memory.set("preferred_language", "Python")
    memory.set("response_style", "concise")

    print("\nStored Preferences:")
    print("Language:", memory.get("preferred_language"))
    print("Style:", memory.get("response_style"))

    print("\nRestart the program to see persistence.")


if __name__ == "__main__":
    main()
