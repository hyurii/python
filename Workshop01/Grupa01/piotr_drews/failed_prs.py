allPRs = input('Podaj liczbe wszystkich PR: ')
failedS = input('Podaj liczbe niedzialajacych PR S: ')
failedA = input('Podaj liczbe niedzialajacych PR A: ')
failedB = input('Podaj lcizbe niedzialajacych PR B: ')

print 'Wszystkie PR:', allPRs
print 'Procent niedzialajacych PR S:', (float(failedS) / allPRs) * 100, '%'
print 'Procent niedzialajacych PR A:', (float(failedA) / allPRs) * 100, '%'
print 'Procent niedzialajacych PR B:', (float(failedB) / allPRs) * 100, '%'