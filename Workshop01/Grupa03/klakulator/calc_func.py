from math import sqrt


def suma():
    a = float(raw_input("Enter first number: "))
    b = float(raw_input("Enter second number: "))
    z = a + b
    return z


def odejm():
    a = float(raw_input("Enter first number: "))
    b = float(raw_input("Enter second number: "))
    z = a - b
    return z


def mnoz():
    a = float(raw_input("Enter first number: "))
    b = float(raw_input("Enter second number: "))
    z = a * b
    return z


def dziel():
    a = float(raw_input("Enter first number: "))
    b = float(raw_input("Enter second number: "))
    if b == 0:
        return "Not possiblu!"
    else:
        z = a / b
    return z


def pierw():
    a = float(raw_input("Enter first number: "))
    z = sqrt(a)
    return z


def potega():
    a = float(raw_input("Enter first number: "))
    b = float(raw_input("Enter second number: "))
    z = a ** b
    return z

'''
x = float(raw_input("Enter first number: "))
y = float(raw_input("Enter second number: "))
def dzialanie(iDzialanie):
    if iDzialanie == "1":
    print suma (x, y)
    print odejm (x, y)
    print mnoz (x, y)
    print dziel (x, y)
    print pierw (x)
    print potega (x, y)
'''
