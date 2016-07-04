"""Listy"""

import collections

# indeksowanie od 0 jak pan bog przykazal
listaA =[1,3,"ala"]
print listaA[2]
# sortowanie ze zmiana
#listaA.sort()

#sortowanie bez zmian
print sorted(listaA)
# dodawanie do listy. nie mozna w prost. trzeba urzysac dodatliwych komend



#kasowanei

# ## del listaA
#
print len(listaA)



# ######## slowniki
#mozna definiowac klucze
slownik1 = {"asd":"asdasdasdasd","qwe":2,"zxc":234}
print slownik1["asd"]
#sprawdzic slownik cat ::
#sprawdzic metody slownikow

#dodawanie elemetu do slownika elementu
slownik1["ddd"]=3


#collection metody
print collections.OrderedDict(slownik1)

#tuple ergo krotki

tuple = ("x","c","v","v")
print type(tuple)
print tuple

#zmiana krotki na list
tuple = list(tuple)
print tuple

#set struktura bez duplikatow
print set(tuple)



#if

a=1
b=1

print id(a)
print id(b)

# is w if. nie porownuje wartosci prawdziwych a adres w pamieci. python nie tworzy w pamieci dwoch miejsc ze
#zmienymi takimi samymy

c=1.0
print id(c)

#if i opweratry logicze. doczytac

#if pass to przejdze dalej


# switch
#python tego nie ma szukaj w pp3103 wyjebali bo nie bo nie

#jest workaround

#ze slownikiem i evalem
slownik2 = {1:"1",2:"2",3:"3"}

print eval(slownik2[3])

#z definiowanem funkcji
def dod(x)
    return {
        1:2
        "2":1234
        }.get(x,False)




##
# zadanie:
# 1
# sortowanie bombelkowe
#lista [2,7,1,3]
#
# dodac statusy do raportu korzystajsc z if i innych takich


