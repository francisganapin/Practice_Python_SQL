from collections import Counter

text = 'a b c c a b'
counter = Counter(text.split())

print(counter)
print(counter['a'])