'''
Created on 4 lip 2016

@author: Tomek

'''

moron = False

try:
    total = int(raw_input("Podaj liczbe PRek: "))
    prS = int(raw_input("Ilosc S PRs: "))
    prA = int(raw_input("Ilosc A PRs: "))
    prB = int(raw_input("Ilosc B PRs: "))
except ValueError:
    print "It is not a number, faggot!"
    moron = True

if not moron:
    if prS > total or prA > total or prB > total:
        print "Number of S or A or B PRs is bigger than number of total PRs. It is not possible, faggot!"
        moron = True
    elif (prS + prA + prB) > total:
        print "Sum of S or A or B PRs is bigger than number of total PRs. It is not possible, faggot!"
        moron = True
    elif prS < 0 or prA < 0 or prB < 0 or total < 0:
        print "You gave somewhere a negative number, faggot!"
        moron = True

if not moron:
    print ("There is"), round(((float(prS))/(float(total)))*100, 2), "% of S PRs in database."
    print ("There is"), round(((float(prA))/(float(total)))*100, 2), "% of A PRs in database."
    print ("There is"), round(((float(prB))/(float(total)))*100, 2), "% of B PRs in database."
else:
    print "Something went wrong! You are a moron!"
