'''
Created on 3 lip 2016

@author: Magda
'''
#Zmienne
prAll = input("Podaj ilosc wszystkich PRek: ")
prA= float(input("Podaj ilosc PRek A: "))
prB= float(input("Podaj ilosc PRek B: "))
prS= float(input("Podaj ilosc PRek S: "))

#obliczenia %
procA=int((prA/prAll) * 100)
procB=int((prB/prAll) * 100)
procS=int((prS/prAll) * 100)

# Wydruk
print "\nilosc wszystkich PRek: " + str(prAll)
print "Procent PRek A: ", int(procA), "%"
print "Procent PRek B: ", int(procB), "%"
print "Procent PRek S: ", int(procS), "%"

input ("\nNacisnij ENTER aby zakonczyc")