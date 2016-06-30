'''
Created on 29 cze 2016
@author: Adam

  Napisac skrypt ktory pyta nas o:
  1. ilosc wszystkich PRek:
  2. ilosc Fail A
  3. ilosc Fail B
  4. ilosc Fail S
  i drukuje % wszystkich prek i fail S/A/B
'''
PrsAll = input("Enter number of all PRs: ")
FailA = input("Enter number of Fail A: ")
FailB = input("Enter number of Fail B: ")
FailS = input("Enter number of Fail S: ")

print "Percentage of Fail A = ", (float(FailA)/PrsAll)*100, "%"
print "Percentage of Fail B = ", (float(FailB)/PrsAll)*100, "%"
print "Percentage of Fail S = ", (float(FailS)/PrsAll)*100, "%"
