def f1(func):
    def wrapper():
        func()
        print("Started")
        print("Ended")
        func()
    return wrapper

@f1
def f():
    print("Hello")
f()

