'''
Created on 25 sie 2016

@author: Zablodan
'''
import psycopg2
from openpyxl.reader.excel import load_workbook
import time
from idlelib.configDialog import is_int


def cvtoNotTested(cur, table):
    cur.execute("UPDATE " + table + " SET rtrt_filename='NOT TESTED' WHERE tstid LIKE 'cvto%'")


def excelToDB(cur):
    location = "IntegrationTestsControl_CONN.xlsx"
    wb = load_workbook(location)
    ws = wb['IntegrationTestsControl_CONN']

    cur.execute("CREATE TABLE IntegrationTestsControl_CONN_" + time.strftime("%Y_%m_%d") +
                " (nr serial PRIMARY KEY," +
                " architecture_filename text," +
                " interface_name text," +
                " tstid text," +
                " rtrt_filename text);")

    for row in ws.rows:
        if is_int(row[0].value):
            cur.execute("INSERT INTO IntegrationTestsControl_CONN_" + time.strftime("%Y_%m_%d") +
                        " (architecture_filename, interface_name, tstid, rtrt_filename)" +
                        " VALUES (%s, %s, %s, %s)", (row[1].value, row[2].value, row[3].value, row[4].value))
    return "IntegrationTestsControl_CONN_" + time.strftime("%Y_%m_%d")

if __name__ == '__main__':
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='dadasus21', host='localhost', port='5432')
    except psycopg2.DatabaseError as e:
        print 'cos nie poszlo:' + str(e)

    cur = conn.cursor()
    table = excelToDB(cur)
    cvtoNotTested(cur, table)
    conn.commit()
    conn.close()
    print "end"
