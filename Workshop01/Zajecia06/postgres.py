'''
Created on 25 08 2016

@author: Tomek

'''

import psycopg2

try:
    conn = psycopg2.connect(database='postgres', user='postgres',password='root',host='localhost',port='5432')
    print "Good"
except:
    print "Error"

cur = conn.cursor()

cur.execute("SELECT * FROM moja")
result = cur.fetchall()

#cur.execute("INSERT INTO moja VALUES (3,'test')")
#conn.commit()

print result

conn.close()