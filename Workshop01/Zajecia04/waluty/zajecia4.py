'''
Created on 28 lip 2016

'''
import pickle
import * from python4

file =  open("plik.txt", "r") 

xtr = pickle.load(file)

file.close()

x = xtr["PLN"]

y = xtr["CHR"]

xtr["CHR"] = x
xtr["PLN"] = y


writeFile(xtr)
