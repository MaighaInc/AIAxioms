state=0
for c in 'ab': state=1 if c=='a' else 2
print(state==2)