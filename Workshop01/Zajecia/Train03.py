'''
Created on 17 cze 2016

@author: giberkrz
'''

spam = input("Podaj ilosc jaj:") # Podajemy 2
spam = str(spam)
spam = spam + "0"
eggs = int(spam) + 3
print float(eggs)

x = 1.212312313123123


print "Jeden %0.2f" % x
print "Jeden".format(0, x)

zmiennDruga = "zmienna"

print zmiennDruga[:5:2]

zmiennTrzecia = str(5)
zmiennaJeden = 1.1

a, b = 1, 2
a = b = 2
print a
print b

# zmienna = 1**2%2
# zmienna = zmienna + 1



suma = zmiennTrzecia + str(float(8)) + "Fos"
print suma

print type(zmiennDruga)
print type(zmiennTrzecia)
print type(zmiennaJeden)
'''

if __name__ == '__main__':
    pass

print "asd"
print 12

print globals()
'''
# asdas


imie = raw_input("Podaj: ")
print imie
