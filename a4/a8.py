freq = {}

arr = [1,2,2,3,3,3]


for item in arr:
    if item not in freq:
        freq[item] = 1
    else:
        freq[item] += 1

print(freq)