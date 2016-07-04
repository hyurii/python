'''
Created on 17 cze 2016

@author: Shaomie
'''
A = int(raw_input('Podaj ile PRek w solved: '))
B = int(raw_input('Podaj ile PRek w failed: '))
S=A+B
ap=int((A*100)/S) 
bp=int((B*100)/S) 
print "Procent Prek w solved to: " , ap , "%"
print "Procent Prek w failed to: " , bp , "%"

