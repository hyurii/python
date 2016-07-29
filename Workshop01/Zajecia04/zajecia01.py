'''
Created on 28 lip 2016

@author: giberkrz
'''
import pickle, cPickle, shelve
import json

"""file = open("nazwa.txt","a")

str= "Zajecia tral;ala \n nhjdhdhdhg"
file.write(str)

file.close()

file = open("nazwa.txt","r+")

xtr = file.read().split("\n")

print xtr

print "POL".join(xtr)


file.close()
"""

doc = {1:"dfsdf",2:"sdaf",3:4444}

file = open("asd.txt","wb")
pickle.dump(doc, file)

file.close()


file = open("asd.txt","rb")
xtr = pickle.load(file)
print type(xtr)

file.close()

"""doc = {1:"dfsdf",2:"sdaf",3:4444}
file = open("asddd.json","wb")
print json.dump(doc,file)
file.close()"""

