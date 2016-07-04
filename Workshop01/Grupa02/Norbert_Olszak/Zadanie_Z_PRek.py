'''
Created on 19 cze 2016

@author: Norbert Olszak
'''

SumaPR_ABS= input('ilosc wszystkich PRek = ')
IloscPR_A= input('ilosc Fail A = ')
IloscPR_B= input('ilosc Fail B = ')
IloscPR_S= input('ilosc Fail S = ')

ProcentPR_ABS= float(IloscPR_A + IloscPR_B + IloscPR_S) / SumaPR_ABS
ProcentPR_A= float(IloscPR_A) / SumaPR_ABS
ProcentPR_B= float(IloscPR_B) / SumaPR_ABS
ProcentPR_S= float(IloscPR_S) / SumaPR_ABS

print(str('\n' + 'Procent PR ABS = ') + '{0:.0%}'.format(ProcentPR_ABS))
print(str('\n' + 'Procent PR A = ') + '{0:.0%}'.format(ProcentPR_A))
print(str('Procent PR B = ') + '{0:.0%}'.format(ProcentPR_B))
print(str('Procent PR S = ') + '{0:.0%}'.format(ProcentPR_S))
