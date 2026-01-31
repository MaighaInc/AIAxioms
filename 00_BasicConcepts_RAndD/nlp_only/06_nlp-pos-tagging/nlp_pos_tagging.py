def pos(w): return 'VERB' if w.endswith('ing') else 'NOUN'
print([(w,pos(w)) for w in ['running','dog']])