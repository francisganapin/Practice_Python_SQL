from collections import Counter

def most_frequet(arr):
    freq = Counter(arr)
    return max(freq,key=freq.get)

arr = [1,2,2,3,4,4,4]
print(most_frequet(arr))