'''
Created on 17 cze 2016

@author: giberkrz
'''
# Komentarz
# int()

spam = input("Podaj ilosc jaj:") # Podajemy 2
spam = str(spam)
spam = spam + "0"
eggs = int(spam) + 3
print float(eggs)


z, y = 2, 3

z = y = 2
print z+1
print y

z = input("Podaj")
print z

zmiennaJeden = str(1)
zmiennaDwa = "String"
zmiennaTrzecia = 2.2

suma = zmiennaJeden + str(float(2))
suma = float(suma) + 2**2
# pow() sqrt()
print suma

print type(zmiennaJeden)
print type(zmiennaDwa)
print type(zmiennaTrzecia)

if __name__ == '__main__':
    pass

print "Pierwszy program"
'''
print globals()
'''