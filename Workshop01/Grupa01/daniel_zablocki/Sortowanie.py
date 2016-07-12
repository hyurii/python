'''
Created on 30 cze 2016

@author: zablodan
'''


def inputInt(Text):
    while True:
        try:
            In = int(raw_input(Text))
            break
        except ValueError:
            print('To nie liczba!')
            continue
    return In

while True:
    number = inputInt('Podaj liczbe sortowanych liczb: ')
    if number <= 0:
        print 'Podaj liczbe dodatnia!'
        continue
    break
list = []
for i in range(int(number)):
    list.append(inputInt('Podaj nastepna liczbe: '))

work = 1
change = 0

while (work):
    for x in range(0, len(list) - 1):
        if (list[x] > list[x + 1]):
            temp = list[x + 1]
            list[x + 1] = list[x]
            list[x] = temp
            change = change + 1
    if change == 0:
        work = 0
    change = 0
print list
