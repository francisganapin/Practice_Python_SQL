from  collections import Counter

with open('a1.txt','r',encoding='utf-8') as f:
    words = f.read().lower().split()


word_freq = Counter(words)
print(word_freq.most_common(5))