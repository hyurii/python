'''
Created on 29 lip 2016

@author: giberkrz
'''
import pickle

def writeDict(x):
    plik = open("plik.txt", "wb")
    pickle.dump(x, plik, pickle.HIGHEST_PROTOCOL)
    plik.close()

if __name__ == '__main__':
    writeDict({"CHF": 2.33, "PLN": 4.55, "GBP": 5.66})
