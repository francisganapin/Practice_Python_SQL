import json


def outer(x):
    def inner(y):
        return x + y
    return inner


f = outer(10)


json.dumps(f)