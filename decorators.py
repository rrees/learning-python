
def uppercase(f):
    return lambda x: f(x).upper()

@uppercase
def greet(name):
    return "Hello " + name
