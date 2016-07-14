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


def odejmowanie():
    
    liczba_A = inputInt("Podaj liczbe bazowa: ")
    liczba_B = inputInt("Podaj liczbe odejmowana: ")
    
    wynik = liczba_A - liczba_B
    return wynik
    # test return str(liczba_A) + " - " + str(liczba_B) + " = " + str(wynik)
    
    
def dzielenie():
    liczba_A = inputInt("Podaj dzielnik: ")
    liczba_B = inputInt("Podaj dzielna: ")
   
    wynik = liczba_A / liczba_B
    return wynik
 #   return str(liczba_A) + " / " + str(liczba_B) + " = " + str(wynik)

def potega():
    liczba_A = inputInt("Podaj liczbe bazowa: ")
    liczba_B = inputInt("Podnosze do potegi: ")
  
    wynik = liczba_A ** liczba_B
    
   # return str(liczba_A) + " ** " + str(liczba_B) + " = " + str(wynik)
    return wynik