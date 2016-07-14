# sortowanie bombelkowe
#lista [2,7,1,3]

lista = [2,7,1,3,5,8,0,10]
print lista
#print len(lista)


koniec = 1
zmiana = 0

while (koniec):
    for i in range(0, len(lista)-1):
        print lista[i]
        print lista[i+1]
        if (lista[i] > lista[i + 1]):
            #print i
            temp = lista[i + 1]
            print "to jest temp"
            print temp
            lista[i + 1] = lista[i]
            lista[i] = temp
            zmiana = zmiana + 1
          #  print "zmiana "
          #  print zmiana
    if zmiana == 0:
        koniec = 0
        print "koniec jest zerowany"
    zmiana = 0
print "koniec"
print lista