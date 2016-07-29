from valuty import *

try:
    fileN = open("plik.txt", "rb")
    x = pickle.load(fileN)
except:
    print "Something is wrong with file!"
else:
    currency = raw_input("Which currency do you want to change: EUR, PLN, CHF")
    kwota = float(raw_input("Value: "))

    x[currency] = kwota
    fileN.close()
    writeDict(x)
