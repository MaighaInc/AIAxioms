Autonomous AI Platform
=====================

This is a full teaching-first autonomous AI platform
combining Agents, RAG, Memory, and APIs.

Requirements:
------------
- Python 3.9+
- pip

Setup:
------
pip install -r requirements.txt

Run:
----
uvicorn platform:app --reload

Endpoints:
----------
GET  /           -> health check
POST /ask        -> ask the platform

Example:
--------
POST /ask
{
  "prompt": "What is RAG?"
}

Response:
---------
{
  "response": "Answer based on docs: RAG combines retrieval with generation."
}

Learning Objective:
-------------------
Understand how production AI systems
combine planning, grounding, memory,
and deployment.
