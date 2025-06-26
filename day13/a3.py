words = ['cat','window','defenestrate']

for w in words:
    if len(w) > 5:
        print(w,'is a long word')
    elif len(w) < 5:
        print(w,'is a short word')