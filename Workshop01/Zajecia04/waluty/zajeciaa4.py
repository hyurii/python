'''
Created on 28 lip 2016

'''
import pickle
from python4 import * 

file =  open("plik.txt", "r") 

xtr = pickle.load(file)

file.close()

x = xtr["PLN"]

y = xtr["CHF"]

xtr["CHF"] = x
xtr["PLN"] = y

writeFile(xtr)
