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
        print addition()
    elif Zmienna =="O":
        print subtraction()
    elif Zmienna=="M":
        print multiplication()
    elif Zmienna=="D":
        print division()
    elif Zmienna == "W":
        print roots()
    elif Zmienna == "T":
        print exponentiation()

