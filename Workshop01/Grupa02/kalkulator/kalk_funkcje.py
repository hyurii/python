'''
Created on 15 lip 2016

@author: Adam
'''
import math

from math import sqrt
def dodawanie():
    x = float(input("Podaj piersza dodawana liczbe: "))
    y = float(input("Podaj druga dodawana liczbe: "))
    suma = x+y
    return suma

def odejmowanie():
    x = float(input("Podaj liczbe od ktorej odejmujesz: "))
    y = float(input("Podaj liczbe ktora odejmujesz: "))
    roznica = x-y
    return roznica

def mnozenie():
    x = float(input("Podaj piersza mnozona liczbe: "))
    y = float(input("Podaj druga mnozona liczbe: "))
    iloczyn = x*y
    return iloczyn

def dzielenie():
    x = float(input("Podaj piersza liczbe (dzielona): "))
    y = float(input("Podaj druga liczbe (dzielnik): "))
    iloraz = x/y
    return iloraz

def potegowanie():
    x = float(input("Podaj postawe potegi: "))
    y = float(input("Podaj wykladnik potegi: "))
    potega = pow(x,y)
    return potega

def pierwiastkowanie():
    x = float(input("Podaj postawe potegi: "))
    pierwiastek = sqrt(x)
    return pierwiastek

x=2
y=2
print dodawanie(x,y)
print odejmowanie(x,y)
print mnozenie(x,y)
print dzielenie(x,y)
print potegowanie(x,y)
print pierwiastkowanie(x,y)