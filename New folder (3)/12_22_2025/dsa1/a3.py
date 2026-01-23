import bisect

a = [2,4,6,8,10]

print(6 in a)

print(a.count(7) > 0)


pos = bisect.bisect_left(a,8)

print('Found at index:',pos)