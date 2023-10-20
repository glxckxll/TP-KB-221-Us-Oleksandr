def sum(x, y):
    return x + y

def min(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ZeroDivisionError("На нуль не можна ділити")
    return x / y
