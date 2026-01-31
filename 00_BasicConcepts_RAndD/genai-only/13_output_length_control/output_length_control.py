def llm(prompt):
    return f"[GENAI OUTPUT] {prompt}"


if __name__ == "__main__":
    prompt = "Demo prompt for output_length_control"
    print(llm(prompt))
