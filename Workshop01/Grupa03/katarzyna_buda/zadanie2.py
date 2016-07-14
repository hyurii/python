'''
Created on 17 cze 2016 updated  12 lipca 2016

@author: Shaomie
'''
ALL = raw_input('Podaj ilosc PRek ogolnie ')

while ALL.isdigit() != True:
    ALL = raw_input('Podaj ilosc PRek ogolnie ')
A = raw_input("Podaj solved: ")
B = raw_input("Podaj failed: ")

while A.isdigit() != True:
    A = raw_input("Podaj solved, ale liczbe dodatnia: ")
while B.isdigit() != True:
    B = raw_input("Podaj failed, ale liczbe dodatnia: ")

ALL=int(ALL)
A=int(A)
B=int(B)

while (A+B) != ALL:
    A = raw_input("Cos poszlo nie tak! Podaj liczbe dodatnia PRek solved raz jeszcze: ")
    B = raw_input("Cos poszlo nie tak! Podaj liczbe dodatnia PRek failed raz jeszcze: ")
    while A.isdigit() != True:
        A = raw_input("podaj solved, ale liczbe: ")
    while B.isdigit() != True:
        B = raw_input("podaj failed, ale liczbe: ")
    A = int(A)
    B = int(B)

ap=int((A*100)/ALL)
bp=int((B*100)/ALL)
print "Procent Prek w solved to: " , ap , "%"
print "Procent Prek w failed to: " , bp , "%"







