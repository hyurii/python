""" Funkcja odejmowania, dzielenia i potegowania"""
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

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
