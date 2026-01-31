def ngrams(w,n): return [tuple(w[i:i+n]) for i in range(len(w)-n+1)]
print(ngrams('nlp',2))