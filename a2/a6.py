def my_decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper


@my_decorator
def hello():
    print('Hello')

hello()