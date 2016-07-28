'''
Created on 28 lip 2016

@author: zablodan
'''
import pickle

def ReadFile():
    file = open("PLIK.txt", "r+")
    load = pickle.load(file)
    return load

def zmiana():
    szukana = raw_input("Podaj walute do zmiany: ")
    wartosc = raw_input("Podaj nowa wartosc: ")
    
    load = ReadFile()
    
    for x in load:
        if x == szukana:
            load[x] = wartosc
    print load
    
    WriteFile(load)
    


