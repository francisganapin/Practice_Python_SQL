def add(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b


operation = {
    "add":add,
    "sub":sub,
    "mul":mul
}

print(operation['add'](5,3))
print(operation['mul'](4,2))