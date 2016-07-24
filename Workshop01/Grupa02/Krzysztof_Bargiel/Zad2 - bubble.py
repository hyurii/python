# Bubble sort
import random


def add_random_values(size, begin, end):
    tab = []
    while size > 0:
        tab.append(random.randint(begin, end))
        size -= 1

    return tab

def bubble_sort(tab):
    for i in range(len(tab)):
        j = len(tab) -1
        while j>i:
            if tab[j]<tab[j-1]:
                temp = tab[j]
                tab[j] = tab[j-1]
                tab[j-1] = temp
            j -= 1
    return tab

tab = add_random_values(10, 1, 10)

print tab

tab = bubble_sort(tab)

print tab
