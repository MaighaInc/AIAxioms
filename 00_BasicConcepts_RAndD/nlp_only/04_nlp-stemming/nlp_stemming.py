def stem(w):
    return w[:-3] if w.endswith('ing') else w
print([stem(w) for w in ['running','play']])