'''
Created on 3 lip 2016

@author: solonzie
'''


'''
 zadadanie domowe ;)
 tortoise sie wypieprzyl na zmiennej homedrive=u: nie ma pojecia skad to gowno sie wzielo niemniej prawdopodniue trzeba bedzie przytargac inny sprzet zamiast jakiego sluzbowego gowna

    - Zrobic zadanie w domu i zaladowac na repo:
        Napisac skrypt ktory pyta nas o:
        1. ilosc wszystkich PRek:
        2. ilosc Fail A
        3. ilosc Fail B
        4. ilosc Fail S
        i drukuje % wszystkich prek i fail S/A/B

'''
aa = input ("Podaj ilosc wszystkich PRek: ")
s = input ("Podaj ilosc PRek Fail typu S: ")
a = input ("Podaj ilosc PRek Fail typu A: ")
b = input ("Podaj ilosc PRek Fail typu B: ")

sab = s+a+b

print
print "Wszystkich PRek z Fail dowolnego typu wyszlo", sab, "co stanowi", sab*100/aa , "%"
print "Procentowo rozklada sie to nastepujaco:"
print "Fail'i typu S:", s*100/aa , "%"
print "Fail'i typu A:", a*100/aa , "%"
print "Fail'i typu B:", b*100/aa , "%"

