# -*- coding: utf-8 -*-
'''
Created on 14 lip 2016

@author: giberkrz
'''

print "kiełbasa".decode('utf-8')

def asn(a,b):
    print locals().values()
    z = a+1
    y = b+1
    return z,y

w,e = asn(1,2)

print w
print e


# petle

#lista = [2,4,6]

rangex1 = xrange(10)
range1 = range(10)

print rangex1
print range1


for x in xrange(10):
    if x == 5:
        break
    print x

for x in range(10):
    print x
    
# iter

iterator = [1,2,3]

itrea = iter(iterator)

print itrea.next()
print itrea.next()

def gener(asd):
    for x in range(5):
        if x == 3:
            yield "oko"
        yield x

z = gener(1)

print type(z)

print z.next()
print z.next()
print z.next()
print z.next()