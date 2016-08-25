'''
Created on 25 sie 2016

@author: giberkrz
'''

import psycopg2

try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='', host='localhost', port='5432')
except psycopg2.DatabaseError as e:
    print 'cos nie poszlo' + str(e)

cur = conn.cursor()

cur.execute("SELECT * FROM moja;")

wynik = cur.fetchall()

#cur.execute("INSERT INTO moja VALUES(3,'tekst')")

conn.commit()

print wynik



#cur.executemany(query,tabela)

conn.close()