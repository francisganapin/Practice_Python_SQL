a = 1
b = 2
c = 3

if all(n > 0 for  n in [a,b,c]):
    print('all positive')
else:
    print('someone was negative')