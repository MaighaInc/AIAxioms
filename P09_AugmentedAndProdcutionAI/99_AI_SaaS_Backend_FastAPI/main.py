"""
AI SaaS Backend using FastAPI
----------------------------
This program demonstrates how
an AI model is deployed as a
production-ready API service.

Author: AI Course
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI SaaS Backend")


# -------- AI MODEL --------
class SimpleAIModel:
    def generate(self, text: str) -> str:
        return f"AI Response: {text.upper()}"


ai_model = SimpleAIModel()


# -------- REQUEST / RESPONSE --------
class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    response: str


# -------- API ENDPOINT --------
@app.post("/generate", response_model=PromptResponse)
def generate_text(request: PromptRequest):
    result = ai_model.generate(request.prompt)
    return {"response": result}


@app.get("/")
def health_check():
    return {"status": "AI SaaS Backend is running"}
