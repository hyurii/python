import psycopg2

try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='kgbms3', host='localhost', port='5432')
except psycopg2.DatabaseError as e:
    print 'cos nie poszlo' + str(e)
    
cur = conn.cursor()

cur.execute("DELETE FROM zadanie_bazy_danych WHERE lala='Test_Integration.html';")


conn.commit()

cur.execute("SELECT * FROM zadanie_bazy_danych")

wynik = cur.fetchall()
conn.commit()
print wynik

conn.close() 