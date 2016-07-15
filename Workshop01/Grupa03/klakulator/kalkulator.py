'''
Created on 15 lip 2016

@author: giberkrz
'''
from calc_func import *

Zmienna = ""
while Zmienna != "X":      
    print "Dostepne dzialania: "
    print "[P] dodawanie "
    print "[O] odejmowanie "
    print "[M] mnozenie "
    print "[D] dzielenie"
    print "[W] pierwiastek "
    print "[T] potega"
    print "[X] wyjscie"

    Zmienna=raw_input("Podaj dzialanie jakie chcesz wykonac: ")
    if Zmienna == "P":
        print suma()
    elif Zmienna =="O":
        print odejm()
    elif Zmienna=="M":
        print mnoz()
    elif Zmienna=="D":
        print dziel()
    elif Zmienna == "W":
        print pierw()
    elif Zmienna == "T":
        print potega()

