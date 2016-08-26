'''
Created on 26 sie 2016

@author: giberkrz
'''

import psycopg2

try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='kgbms3', host='localhost', port='5432')
except psycopg2.DatabaseError as e:
    print "BL:ad" + str(e)

cur = conn.cursor()

cur.execute("SELECT * FROM moja;")

lista = cur.fetchone()

print lista
lista = cur.fetchone()
print lista

cur.execute("INSERT INTO moja VALUES (4,'grupa03');")

cur.execute("SELECT * FROM moja;")

lista = cur.fetchall()

print lista

conn.commit()

cur.executmany(query, tabela)

conn.close()