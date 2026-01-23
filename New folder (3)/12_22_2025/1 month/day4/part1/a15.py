from collections import Counter

text = "python is easy to learn and python is powerful"

words = text.split()

word_freq = Counter(words)

print(word_freq)