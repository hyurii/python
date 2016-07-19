from math import sqrt


def addition():
    try:
        a = float(raw_input("Enter first number: "))
        b = float(raw_input("Enter second number: "))
    except ValueError:
        z = "It is not a number!"
    else:
        z = a + b
    return z


def subtraction():
    try:
        a = float(raw_input("Enter first number: "))
        b = float(raw_input("Enter second number: "))
    except ValueError:
        z = "It is not a number!"
    else:
        z = a - b
    return z


def multiplication():
    try:
        a = float(raw_input("Enter first number: "))
        b = float(raw_input("Enter second number: "))
    except ValueError:
        z = "It is not a number!"
    else:
        z = a * b
    return z


def division():
    try:
        a = float(raw_input("Enter first number: "))
        b = float(raw_input("Enter second number: "))
    except ValueError:
        z = "It is not a number!"
    else:
        if b == 0:
            z = "Not possible!"
        else:
            z = a / b
    return z


def roots():
    try:
        a = float(raw_input("Enter a number: "))
    except ValueError:
        z = "It is not a number!"
    else:
        z = sqrt(a)
    return z


def exponentiation():
    try:
        a = float(raw_input("Enter first number: "))
        b = float(raw_input("Enter second number: "))
    except ValueError:
        z = "It is not a number!"
    else:
        z = a ** b
    return z
