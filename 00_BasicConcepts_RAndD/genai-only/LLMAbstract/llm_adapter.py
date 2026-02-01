from mock_llm import m_llm
from local_llm import l_llm
from real_llm import r_llm

from validate import validate_output
import os

def llm(prompt: str) -> str:
    backend = os.getenv("GENAI_BACKEND", "mock")

    if backend == "openai":
        # Drop-in location for real OpenAI call
        return r_llm.llm(prompt)

    if backend == "local":
        # Drop-in location for Ollama / llama.cpp / LM Studio
        return l_llm.llm(prompt)

    return m_llm.llm(prompt)
