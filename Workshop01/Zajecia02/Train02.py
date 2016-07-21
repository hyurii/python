'''
Created on 4 lip 2016

@author: giberkrz
'''
import collections


'''Listy'''
'''
listPierwsa = [1,"sdaasd",2,[2,3]]

print listPierwsa[3][1]
'''
'''
print listPierwsa[0]

listPierwsa.append("object")

listPierwsa.insert(0, "0")'''

#print listPierwsa[1][::2]
'''
print listPierwsa.sort()
print listPierwsa
'''
'''
print sorted(listPierwsa)

print listPierwsa

del(listPierwsa[1])

print listPierwsa

len(listPierwsa)
'''
#print sum(listPierwsa)

""" Slowniki"""

slownikP = {"a":23, 4: "cokolwiek", "123":22}
'''
print slownikP

print slownikP.values()[:2]

print slownikP.keys()

slownikP["ccc"] = "asd"
'''

print collections.OrderedDict(slownikP)

"tuple"

tupleP = ("x","c","v","x","c")



#tupleP[1]="s"



tupleP = list(tupleP)

print tupleP


''' set '''

slownikP = {1:2,2:3,4:5}

print set(slownikP.values())

print slownikP

# is ==

asd = 1
ddd = 1

print id(asd)
print id(ddd)



if 1==1 and 2==3 or 3==3:
    print 2
else:
    print "NIE"
    
    
slownik = {0:"globals()",1:"b",2:"c"}


print eval(slownik[0])


def dom(do):
    return{"1":1,
           "2":2           }.get(do,False)

print dom("2")


if (1) and (2+2 >3):
    print True
else:
    print False




