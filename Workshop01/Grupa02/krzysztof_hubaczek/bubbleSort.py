def bubbleSort(lista):
    for reszta in range(len(lista) - 1, 0, -1):
        for i in range(reszta):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


def shortBubbleSort(lista):
    zamiana = True
    raszta = len(lista) - 1
    while raszta > 0 and zamiana:
        zamiana = False
        for i in range(raszta):
            if lista[i] > lista[i + 1]:
                zamiana = True
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
        raszta -= 1


lista = [4, 6, 7, 1]
bubbleSort(lista)
print(lista)

lista = [4, 6, 7, 1]
shortBubbleSort(lista)
print(lista)
