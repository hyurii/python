'''
Created on 25 sie 2016

@author: Renia
'''

import psycopg2

try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="pdriver", host="Localhost", port="5432")
except:
    print "cos nnie dziala"
    

#login = raw_input("Podaj login")
#haslo = raw_input("Podaj haslo")

cur = conn.cursor()
cur.execute("SELECT * FROM zadanie")
wynik = cur.fetchall()
print wynik

def sprawdz_dane(login,haslo):
    for i in wynik:
        if login in i:
            if haslo in i:
                return "mozesz wejsc"
            else:
                "Haslo niepoprawne"
        else:
            return "NIe ma takiego loginu"
        
print sprawdz_dane("login1", "haslo9")
        
            
    
    


if __name__ == '__main__':
    pass