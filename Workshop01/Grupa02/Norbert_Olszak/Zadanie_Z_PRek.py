'''
Created on 19 cze 2016

@author: Norbert Olszak
'''

#Logic for "ilosc wszytkich PRek"
import sys

while True:
   try:
      SumaPR_ABS= int(input('ilosc wszystkich PRek = '))
   except (ValueError, SyntaxError, NameError, TypeError):
      print(str('\n' + 'Niepoprawny znak, prosze wprowadzic wartosc liczbowa' + '\n'))
      continue
   if SumaPR_ABS <0:
	  print(str('\n' + 'Bledna wartosc, prosze wprowadzic wartosc liczbowa =>0' + '\n'))
	  continue
   else:
      break

#Logic for "ilosc Fail A"
while True:
   try:
      IloscPR_A= int(input('ilosc Fail A = '))
   except (ValueError, SyntaxError, NameError, TypeError):
      print(str('\n' + 'Niepoprawny znak, prosze wprowadzic wartosc liczbowa' + '\n'))
      continue
   if IloscPR_A <0:
	  print(str('\n' + 'Bledna wartosc, prosze wprowadzic wartosc liczbowa =>0' + '\n'))
	  continue
   if SumaPR_ABS < IloscPR_A:
	  print(str('\n' + 'Suma PRek Przekroczona, prosze wprowadzic wartosc liczbowa nie wieksza niz ' + str(SumaPR_ABS) + '\n'))
	  continue   
   else:
      break

#Logic for "ilosc Fail B"
SumCheck_B= SumaPR_ABS - IloscPR_A

while True:
   try:
      IloscPR_B= int(input('ilosc Fail B = '))
   except (ValueError, SyntaxError, NameError, TypeError):
      print(str('\n' + 'Niepoprawny znak, prosze wprowadzic wartosc liczbowa' + '\n'))
      continue
   if IloscPR_B <0:
	  print(str('\n' + 'Bledna wartosc, prosze wprowadzic wartosc liczbowa =>0' + '\n'))
	  continue
   if SumCheck_B < IloscPR_B:
	  print(str('\n' + 'Suma PRek Przekroczona, prosze wprowadzic wartosc liczbowa nie wieksza niz ' + str(SumCheck_B) + '\n'))
	  continue   
   else:
      break

#Logic for "ilosc Fail S"
SumCheck_S= SumaPR_ABS - IloscPR_A - IloscPR_B
while True:
   try:
      IloscPR_S= int(input('ilosc Fail S = '))
   except (ValueError, SyntaxError, NameError, TypeError):
      print(str('\n' + 'Niepoprawny znak, prosze wprowadzic wartosc liczbowa' + '\n'))
      continue
   if IloscPR_S <0:
	  print(str('\n' + 'Bledna wartosc, prosze wprowadzic wartosc liczbowa =>0' + '\n'))
	  continue
   if SumCheck_S < IloscPR_S:
	  print(str('\n' + 'Suma PRek Przekroczona, prosze wprowadzic wartosc liczbowa nie wieksza niz ' + str(SumCheck_S) + '\n'))
	  continue   
   else:
      break

ProcentPR_ABS= float(IloscPR_A + IloscPR_B + IloscPR_S) / SumaPR_ABS
ProcentPR_A= float(IloscPR_A) / SumaPR_ABS
ProcentPR_B= float(IloscPR_B) / SumaPR_ABS
ProcentPR_S= float(IloscPR_S) / SumaPR_ABS

print(str('\n' +  'Procent PR ABS = ') + '{0:.0%}'.format(ProcentPR_ABS))

print(str('\n' + 'Procent PR A = ') + '{0:.0%}'.format(ProcentPR_A))
print(str('Procent PR B = ') + '{0:.0%}'.format(ProcentPR_B))
print(str('Procent PR S = ') + '{0:.0%}'.format(ProcentPR_S))
