def llm(prompt):
    return f"[GENAI OUTPUT] {prompt}"


if __name__ == "__main__":
    prompt = "Demo prompt for memory_recall_prompting"
    print(llm(prompt))
