'''
Created on 29 lip 2016

@author: kiel,norbercik
'''

import pickle


def zapis(dict2):
    plik = open("plik.txt", "wb")
    pickle.dump(dict2, plik, 0)
    plik.close()


if __name__ == '__main__':
    dict2 = {"EUR": 3.99, "PLN": 2.50, "CHR": 10.50} 
    zapis(dict2)


