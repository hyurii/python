'''
Created on 29 lip 2016

@author: giberkrz
'''

import pickle, cPickle ,shelve
import json




dict2 = '{1:"asd",2:123,3:"trorlro"}'
print json.loads(dict2)

"""file = open("pickle.txt","wb")
pickle.dump(dict2, file,0)
file.close()

file = open("pickle.txt","rb")
xtr = pickle.load(file)
print type(xtr)
file.close()
"""



"""file = open("plik01.txt","w")
str = "trolorlo \n asdasddasd"
file.write(str)
file.close()"""

"""file = open("plik01.txt","a")

file.write("sadasd")


file.close()"""