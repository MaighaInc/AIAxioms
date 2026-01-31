import re
text='Hello. How are you? Fine!'
print([s.strip() for s in re.split(r'[.!?]', text) if s.strip()])