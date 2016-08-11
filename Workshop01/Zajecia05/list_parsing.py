
#lista = [[1,2,3],[1,2,"NOT TESTED"],[1,2,3]]


def ListParsing(List):
    i = 0
    newList = []
    for x in range(len(List)):
        for y in range(len(List[1])):
            if List[x][y] == "NOT TESTED":
                i += 1
                newList.append(List[x][y])
    #print i, newList
    return i, newList

#ListParsing(lista)