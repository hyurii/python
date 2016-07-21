'''
Created on 4 lip 2016

@author: giberkrz
'''
import collections

""" Listy """

listaA = [1,3,"asd",2,[1,2]]
print listaA[4][1]

print listaA[2]

listaA[2]="ddd"

listaA.sort()

print sorted(listaA)


print len(listaA)

print listaA

""" Slowniki"""

slownikPierwszy = {"asd":1, 3:"fasdfdf", 4:5}

print slownikPierwszy[3][::2]

slownikPierwszy["ddd"]="dodane"

print slownikPierwszy

print collections.OrderedDict(slownikPierwszy)

print list(slownikPierwszy.values())

""" tuple """

tuple = ("x","c","v","x","c")

print type(tuple)
tuple = list(tuple)
print tuple

""" set"""
print set(tuple)

asd = 1
ddd = 1

print id(asd)
print id(ddd)
# is

if 1==1 and 1==2 or 3!=3:
    # asd asd
    pass

else:
    print "NIE"


slownikA = {"a":"globals()",2:"sda",4:"asd"}

print eval(slownikA["a"])

def dod(x):
    return{1:2,
           "2":3
           }.get(x,False)
           
print dod(1)

liczbaPierwsza = 123
print id(liczbaPierwsza)
stringDrugaa = 122
print id(stringDrugaa)
stringDrugaa = stringDrugaa+1

print id(stringDrugaa)
if liczbaPierwsza == stringDrugaa:
    print 1
if stringDrugaa is liczbaPierwsza:
    print 2
