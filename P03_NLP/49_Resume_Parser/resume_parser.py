"""
Resume Parser (From Scratch)
----------------------------
This program extracts key information
from a resume using NLP techniques.

Author: AI Course
"""

import re


class ResumeParser:
    def __init__(self):
        self.skills = {
            "python", "java", "machine learning",
            "deep learning", "nlp", "data science"
        }

    def extract_email(self, text):
        match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+", text)
        return match.group() if match else None

    def extract_phone(self, text):
        match = re.search(r"\b\d{10}\b", text)
        return match.group() if match else None

    def extract_skills(self, text):
        text_lower = text.lower()
        found = []
        for skill in self.skills:
            if skill in text_lower:
                found.append(skill)
        return found

    def extract_name(self, text):
        lines = text.split("\n")
        return lines[0].strip()

    def parse(self, resume_text):
        return {
            "Name": self.extract_name(resume_text),
            "Email": self.extract_email(resume_text),
            "Phone": self.extract_phone(resume_text),
            "Skills": self.extract_skills(resume_text)
        }


def main():
    print("RESUME PARSER")
    print("--------------")

    resume = """
    John Doe
    Email: john.doe@email.com
    Phone: 9876543210

    Skills:
    Python, Machine Learning, NLP, Data Science

    Experience:
    Worked as an AI Engineer
    """

    parser = ResumeParser()
    parsed = parser.parse(resume)

    print("\nParsed Resume Data:")
    for key, value in parsed.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
