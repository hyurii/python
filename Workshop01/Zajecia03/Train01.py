'''
Created on 30 cze 2016

@author: zablodan
'''
import timeit

'''
import timeit

start = timeit.timeit()


list = [1,3,4,5]



iterator = iter(list)

print iterator.next()
end = timeit.timeit()


print start-end

def generator(sda):
    yield "Krzysiek"
    if (sda):
        yield "DANiel"
    yield "Magda"

x = generator()
print (x)

print x.next()
print x.next()


for x in list:
    print x

size = 0
while size < len(list):
    try:
        print list[size]
        size= size + 1
        break
    except StopIteration:
        print "Koniec"

'''

start = timeit.timeit()
lista = [1,5,6]

x = iter(lista)

def generator():
    for x in [1,2,3]:
        yield x
        
z = generator()

print z.next()
print z.next()
end = timeit.timeit()

print end - start

print x.next()
print x.next()


t = range(10)
print t
t = xrange(10)
print t

for x in xrange(10):
    if x == 5:
        break
    print x


warunek = 0
while warunek < 10:
    warunek+=1
    print warunek


z =4

def asdasd(asd1,asd2):
    global z
    z = 3
    y= asd2
    return z,y
print z
z,x =asdasd(1, 2)
