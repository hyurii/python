def bubbleSort(lista):
    for reszta in range(len(lista) - 1, 0, -1):
        for i in range(reszta):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


lista = [4, 6, 7, 1]
bubbleSort(lista)
print lista
