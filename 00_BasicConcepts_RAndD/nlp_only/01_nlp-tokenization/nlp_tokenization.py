import re
text='Hello NLP World!'
print(re.findall(r"\b\w+\b", text))