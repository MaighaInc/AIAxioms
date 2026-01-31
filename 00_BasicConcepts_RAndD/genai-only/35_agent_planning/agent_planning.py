def llm(prompt):
    return f"[GENAI OUTPUT] {prompt}"


if __name__ == "__main__":
    prompt = "Demo prompt for agent_planning"
    print(llm(prompt))
