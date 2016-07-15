'''
Created on 17 cze 2016 updated  12 lipca 2016

@author: Shaomie
'''

import random

# losowanie liczb oraz zabezpieczenia antymoronowe.

Population = raw_input("In what range of numbers shall I sort? : ")
littlek = raw_input("How many numbers should I choose from whole population? : ")

while Population.isdigit() != True:
    Population = raw_input("Your number population should be positive, please try again: ")
while littlek.isdigit() != True:
    littlek = raw_input("Your sample number should be positive, please try again: ")

Population = int(Population)
littlek = int(littlek)

while Population < littlek:
    Population = raw_input("Your number population should be positive and bigger than your sample, please try again: ")
    littlek = raw_input("Your sample number should be positive and smaller or same as your population, please try again: ")
    while Population.isdigit() != True:
        Population = raw_input("Your number population should be positive, please try again: ")
    while littlek.isdigit() != True:
        littlek = raw_input("Your sample number should be positive, please try again: ")

Population = int(Population)
littlek = int(littlek)

while Population >= littlek:
    X=random.sample(xrange(Population),littlek)
    break

print "Numbers randomly generated from choosen population are: ", X

# sortowanie

cos=littlek

for i in range(1,cos):
    for x in range(0,littlek-1):
        if X[x] > X[x+1]:
            z=X[x]
            X[x]=X[x+1]
            X[x + 1]=z
    cos=cos-1

print "New order of generated numbers is: ", X






