'''
Created on 4 lip 2016

@author: Tomek

if __name__ == '__main__':
    pass
'''

from random import *
from timeit import default_timer as timer

# print "TODO here will be sorting"

# create an array

aArray = []

for x in range(0, 10):
    i = randint(0, 100)
    aArray.append(i)


def sortingBubble():

    start = timer()
    iLen = len(aArray)
    print iLen
    print "Non-sorted array: ", aArray

    for i in range(0, (iLen - 1)):
        for j in range(0, (iLen - 1)):
            if aArray[j] > aArray[j+1]:
                iTemp = aArray[j+1]
                # print "iTemp", iTemp
                aArray[j+1] = aArray[j]
                aArray[j] = iTemp

            print aArray

    print "Sorted array: ", aArray
    end = timer()
    print "Time for bubble sorting: ", (end - start)

def smartBubble():
    start = timer()
    iLen = len(aArray)
    print iLen
    print "Non-sorted array: ", aArray
    nonSorted = 0

    while nonSorted < (iLen - 1):
        nonSorted = 0
        for j in range(0, (iLen - 1)):
            if aArray[j] > aArray[j + 1]:
                # print "j ", j , aArray[j]
                # print "j+1 ", j, aArray[j+1]
                iTemp = aArray[j + 1]
                # print "iTemp", iTemp
                aArray[j + 1] = aArray[j]
                aArray[j] = iTemp
            else:
                # print "nonSorted", nonSorted
                nonSorted += 1

            print aArray

    print "Sorted array: ", aArray
    end = timer()
    print "Time for smart sorting: ", (end - start)

#sortingBubble()
smartBubble()
