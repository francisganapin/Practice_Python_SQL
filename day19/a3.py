a = -1
b = 2 
c = 0 


values = {'a':a,"b":b,"c":c}

non_positive = [name for name,value in values.items() if value <= 0]


if not non_positive:
    print('All positive')
else:
    print(f"the following variable are not positive: {','.join(non_positive)}")