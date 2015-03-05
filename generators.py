
def fib():
    a, b = 0,1
    while True:
        yield a
        a,b = b, a+b

def my_range(lower, upper):
	pass