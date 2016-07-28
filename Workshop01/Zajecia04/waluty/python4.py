'''
Created on 28 lip 2016

@author: Renia
'''

import pickle


dict = {"CHF": 2.33, "PLN": 4.55, "GBP": 5.66}

def writeFile(x):
    plik = open("plik.txt", "w")
    pickle.dump(x, plik)
    plik.close()
    
writeFile(dict)   