stop={'is','the'}
text='nlp is the base'
print([w for w in text.split() if w not in stop])