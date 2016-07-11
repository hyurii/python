'''
Created on 4 lip 2016

@author: Tomek

if __name__ == '__main__':
    pass
'''

total = raw_input("Podaj liczbe PRek: ")
prS = raw_input("Ilosc S PRs: ")
prA = raw_input("Ilosc A PRs: ")
prB = raw_input("Ilosc B PRs: ")

print ("There is"), round(((float(prS))/(float(total)))*100, 2), "% of S PRs in database."
print ("There is"), round(((float(prA))/(float(total)))*100, 2), "% of A PRs in database."
print ("There is"), round(((float(prB))/(float(total)))*100, 2), "% of B PRs in database."
