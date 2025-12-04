def range_sum(prefix,l,r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]

def build_prefix(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    
    for i in range(1,len(arr)):
        prefix[i] = prefix[i -1 ] + arr[i]

    return prefix


arr = [2,4,6,1,3]
prefix = build_prefix(arr)
print(range_sum(prefix,1,3))