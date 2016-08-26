'''
Created on 26 sie 2016

@author: giberkrz
'''

import psycopg2
import hashlib

input_user = "kapitan"
input_password = "dupa123"

passw_md5 = hashlib.md5(input_password).hexdigest()
print passw_md5

try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='kgbms3', host='localhost', port='5432')
except psycopg2.DatabaseError as e:
    print "BL: " + str(e)

cur = conn.cursor()

query = "SELECT user_password FROM users WHERE user_name = '" + input_user + "';"

cur.execute(query)

password_from_db = cur.fetchall()

print password_from_db

password_from_db = password_from_db[0]

print password_from_db

password_from_db = password_from_db[0]

print password_from_db

conn.close()

if password_from_db == passw_md5:
    print "PASSWORD OK"
else:
    print "DDDUPA"
