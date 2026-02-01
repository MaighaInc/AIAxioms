#
#def llm(prompt):
#    return f"[GENAI OUTPUT] {prompt}"
#
#
#if __name__ == "__main__":
#    prompt = "Demo prompt for zero_shot_prompting"
#    print(llm(prompt))


from llm_adapter import ladapter
from validate import validate_output

if __name__ == "__main__":
    prompt = "Demo prompt for zero_shot_prompting"

    response = ladapter.llm(prompt)
    print(response)
    validate_output(response, prompt)

