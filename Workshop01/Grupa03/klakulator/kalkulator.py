'''
Created on 15 lip 2016

@author: giberkrz
'''

if __name__ == '__main__':
    
    print "Dostepne dzialania: "
    print "[P] dodawanie "
    print "[O] odejmowanie "
    print "[M] mnozenie "
    print "[D] dzielenie"
    print "[W] pierwiastek "
    print "[T] potega"
    
    Zmienna=raw_input("Podaj dzialanie jakie chcesz wykonac: ")
    if Zmienna == "P":
        suma()
    elif Zmienna =="O":
        odejm()
    elif Zmienna=="M":
        mnoz()
    elif Zmienna=="D":
        dziel()
    elif Zmienna == "W":
        pierw()
    elif Zmienna == "T":
        potega()
    
    pass