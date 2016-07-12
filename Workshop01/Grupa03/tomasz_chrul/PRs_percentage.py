'''
Created on 4 lip 2016

@author: Tomek

if __name__ == '__main__':
    pass
'''

moron = False

try:
    total = int(raw_input("Podaj liczbe PRek: "))
except ValueError:
    print "It is not a number, faggot!"
    moron = True

try:
    prS = int(raw_input("Ilosc S PRs: "))
except ValueError:
    print "It is not a number, faggot!"
    moron = True

try:
    prA = int(raw_input("Ilosc A PRs: "))
except ValueError:
    print "It is not a number, faggot!"
    moron = True

try:
    prB = int(raw_input("Ilosc B PRs: "))
except ValueError:
    print "It is not a number, faggot!"
    moron = True

if prS > total or prA > total or prB > total:
    print "Number of S or A or B PRs is bigger than number of total PRs. It is not possible, faggot!"
    moron = True
elif (prS + prA + prB) > total:
    print "Sum of S or A or B PRs is bigger than number of total PRs. It is not possible, faggot!"
    moron = True

if not moron:
    print ("There is"), round(((float(prS))/(float(total)))*100, 2), "% of S PRs in database."
    print ("There is"), round(((float(prA))/(float(total)))*100, 2), "% of A PRs in database."
    print ("There is"), round(((float(prB))/(float(total)))*100, 2), "% of B PRs in database."
else:
    print "Something went wrong! You are a moron!"
