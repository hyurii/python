'''
Created on 14 lip 2016

@author: giberkrz
'''
import funkcje

def podajWartosci():
    dzialanie = 0
    while dzialanie != 7:
        print "1: dodawanie"
        print "2: odejmowanie"
        print "3: mnozenie"
        print "4: dzielenie"
        print "5: potegowanie"
        print "6: pierwiastek"
        print "7: KONIEC"
        
        dzialanie = int(raw_input("Podaj numer akcji ktora chcesz wykonac"))
        if dzialanie == 7:
            print "KONIEC"
        else:
            switch(dzialanie)



def switch(x):
    return {
            1: funkcje.dodaj(),
            2: funkcje.odejmowanie(),
            3: funkcje.pomnoz(),
            4: funkcje.dzielenie(),
            5: funkcje.potega(),
            6: funkcje.pierwiastek()
            }.get(x)

            
podajWartosci()

