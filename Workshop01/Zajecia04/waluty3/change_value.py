from valuty import *


fileN = open("plik.txt", "rb")
x = pickle.load(file)
#print type(x)

currency = raw_input("Which currency do you want to change: EUR, PLN, CHR")
kwota = float(raw_input("Currency: "))

x[currency]= kwota
fileN.close()

writeDict(x)
