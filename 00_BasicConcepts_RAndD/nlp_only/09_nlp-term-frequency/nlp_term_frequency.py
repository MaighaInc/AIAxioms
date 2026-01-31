text='nlp nlp fun'
words=text.split()
print({w:words.count(w)/len(words) for w in set(words)})