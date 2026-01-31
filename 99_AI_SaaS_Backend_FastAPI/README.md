AI SaaS Backend (FastAPI)
========================

This project demonstrates how
AI systems are deployed as
production APIs.

Requirements:
------------
- Python 3.9+
- pip installed

Installation:
-------------
1. Create virtual environment (optional)

   python -m venv venv
   source venv/bin/activate (Linux/macOS)
   venv\Scripts\activate (Windows)

2. Install dependencies

   pip install -r requirements.txt

Running the Server:
-------------------
uvicorn main:app --reload

Access API:
-----------
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

Example Request:
----------------
POST /generate
{
  "prompt": "hello ai"
}

Example Response:
-----------------
{
  "response": "AI Response: HELLO AI"
}

Learning Objective:
-------------------
Understand how AI models are
served as scalable APIs.
