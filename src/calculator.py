def sum(a,b):
    return  a + b

def subtrac(a,b):
    return  a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("La división en cero no esta permitida")
    return a / b
