text='nlp is fun nlp'
words=text.split()
print([words[i-1:i+2] for i,w in enumerate(words) if w=='nlp'])