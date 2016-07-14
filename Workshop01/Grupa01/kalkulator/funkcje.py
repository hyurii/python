'''
Created on 14 lip 2016

@author: zablodan
'''
import math


def inputInt(Text):
    while True:
        try:
            In = int(raw_input(Text))
            break
        except ValueError:
            print('To nie liczba!')
            continue
    return In


def dodaj():
    x1 = inputInt("Podaj pierwsza liczbe: ")
    x2 = inputInt("Podaj druga liczbe: ")
    y = x1 + x2
    return y


def pomnoz():
    x1 = inputInt("Podaj pierwsza liczbe: ")
    x2 = inputInt("Podaj druga liczbe: ")
    y = x1 * x2
    return y


def pierwiastek():
    x = inputInt("Podaj liczbe pierwiastkowana: ")
    s = inputInt("Podaj stopien pierwiastka: ")
    y = math.pow(x, (1.0 / s))
    return y


y = pierwiastek()
print y

y = dodaj()
print y
y = pomnoz()
print y