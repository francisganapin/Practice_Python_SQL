from collections import Counter


def is_anagram(w1,w2):
    return Counter(w1) == Counter(w2)

print(is_anagram('listen','silent'))