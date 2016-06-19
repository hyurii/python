'''
Created on 19 cze 2016

@author: Norbert Olszak
'''

IloscPR_A= 15
IloscPR_B= 10
IloscPR_C= 75

SumaPR_ABC= IloscPR_A + IloscPR_B + IloscPR_C
ProcentPR_A= float(IloscPR_A) / SumaPR_ABC
ProcentPR_B= float(IloscPR_B) / SumaPR_ABC
ProcentPR_C= float(IloscPR_C) / SumaPR_ABC

print(str('Ilosc PR A = ') + str(IloscPR_A))
print(str('Ilosc PR B = ') + str(IloscPR_B))
print(str('Ilosc PR C = ') + str(IloscPR_C))
print('\n' + str('Suma wszystkich PR = ') + str(SumaPR_ABC))
print(str('Procent PR A = ') + '{0:.0%}'.format(ProcentPR_A))
print(str('Procent PR B = ') + '{0:.0%}'.format(ProcentPR_B))
print(str('Procent PR C = ') + '{0:.0%}'.format(ProcentPR_C))
