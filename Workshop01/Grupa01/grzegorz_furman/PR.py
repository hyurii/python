'''
Created on 30 cze 2016

@author: grzegorz

Napisac skrypt ktory pyta nas o:
  1. ilosc wszystkich PRek:
  2. ilosc Fail A
  3. ilosc Fail B
  4. ilosc Fail S
  i drukuje % wszystkich prek i fail S/A/B
'''

pr = input("Enter the number of total PR: ")
a = input("Enter the number of Fail A: ")
b = input("Enter the number of Fail B: ")
s = input("Enter the number of Fail S: ")

print " "
print "Total PR's = ", pr, "(", int((pr*100)/pr), "%", ")"
print "Fail A = ", a, "(", float((a*100)/pr), "%", ")"
print "Fail B = ", b, "(", float((b*100)/pr), "%", ")"
print "Fail S = ", s, "(", float((s*100)/pr), "%", ")"

