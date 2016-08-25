from openpyxl import Workbook
from openpyxl import load_workbook
import psycopg2

location = "IntegrationTestsControl_CONN.xlsx"
wb = load_workbook(location)
ws = wb.active


def tworzenie_listy(ws):
    xls_list = []
    xls_list2 = []
    for x in ws.rows:
        for y in x:
            xls_list2.append(y.value)
        xls_list.append(xls_list2)
        xls_list2 = []
    return xls_list

excelowa_lista = tworzenie_listy(ws)
print excelowa_lista

try:
    conn = psycopg2.connect(database='postgres', user='postgres',password='root',host='localhost',port='5432')
    print "Connected"
except psycopg2.DatabaseError as err:
    print err

cur = conn.cursor()

try:
    stmt = "INSERT INTO excel VALUES (%s, %s, %s, %s, %s)"
    cur.executemany(stmt, excelowa_lista)
    print "Saved"
    conn.commit()
except psycopg2.DatabaseError as err:
    print err
    conn.rollback()

cur.execute("SELECT * FROM excel")
result = cur.fetchall()

print result

conn.close()