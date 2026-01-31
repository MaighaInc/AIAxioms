"""
Autonomous AI Platform
---------------------
A teaching-first, end-to-end platform that combines:
- Agent planning
- Retrieval-Augmented Generation (RAG)
- Long-term memory
- API interface (FastAPI-style)

Author: AI Course
"""

from fastapi import FastAPI
from pydantic import BaseModel
import math
from collections import Counter

# ------------------ MEMORY ------------------
class MemoryStore:
    def __init__(self):
        self.entries = []

    def add(self, text):
        self.entries.append(text)

    def recall(self, k=3):
        return self.entries[-k:]


# ------------------ RAG ------------------
class SimpleRAG:
    def tokenize(self, text):
        return text.lower().split()

    def embed(self, tokens, vocab):
        counts = Counter(tokens)
        return [counts[w] for w in vocab]

    def cosine(self, a, b):
        dot = sum(x*y for x,y in zip(a,b))
        ma = math.sqrt(sum(x*x for x in a))
        mb = math.sqrt(sum(x*x for x in b))
        return dot/(ma*mb) if ma and mb else 0.0

    def retrieve(self, query, docs, top_k=2):
        vocab = set(self.tokenize(query))
        for d in docs:
            vocab.update(self.tokenize(d))
        vocab = list(vocab)

        qv = self.embed(self.tokenize(query), vocab)
        scored = []
        for d in docs:
            dv = self.embed(self.tokenize(d), vocab)
            scored.append((d, self.cosine(qv, dv)))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [d for d,_ in scored[:top_k]]


# ------------------ AGENT ------------------
class PlannerAgent:
    def plan(self, task):
        if "calculate" in task.lower():
            return "use_tool"
        return "use_rag"

class CalculatorTool:
    def run(self, expr):
        try:
            return str(eval(expr))
        except:
            return "calc error"


# ------------------ PLATFORM ------------------
class AutonomousPlatform:
    def __init__(self):
        self.memory = MemoryStore()
        self.rag = SimpleRAG()
        self.planner = PlannerAgent()
        self.tools = {"calculator": CalculatorTool()}
        self.docs = [
            "Machine learning is a subset of artificial intelligence.",
            "RAG combines retrieval with generation.",
            "Agents can plan and act autonomously."
        ]

    def handle(self, prompt):
        decision = self.planner.plan(prompt)

        if decision == "use_tool":
            expr = prompt.lower().replace("calculate", "").strip()
            result = self.tools["calculator"].run(expr)
            self.memory.add(f"calc:{expr}={result}")
            return f"Result: {result}"

        context = self.rag.retrieve(prompt, self.docs)
        recall = self.memory.recall()
        answer = f"Answer based on docs: {' '.join(context)}"
        if recall:
            answer += f" | Memory: {recall}"
        self.memory.add(prompt)
        return answer


# ------------------ API ------------------
app = FastAPI(title="Autonomous AI Platform")
platform = AutonomousPlatform()

class PromptIn(BaseModel):
    prompt: str

class PromptOut(BaseModel):
    response: str

@app.post("/ask", response_model=PromptOut)
def ask(req: PromptIn):
    return {"response": platform.handle(req.prompt)}

@app.get("/")
def health():
    return {"status": "Autonomous AI Platform running"}
