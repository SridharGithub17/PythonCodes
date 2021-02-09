#!/bin/usr/python
#Connect SQL Lite db

import sqlite3
from sqlite3 import Error  

def createConnection(db_file):
    conn = None
    try:
        conn =  sqlite3.connect(db_file)
        print(sqlite3.version)        
        print("Connecton Successful")
        cur = conn.cursor()
        cur.execute("SELECT * FROM CONTACTS")
        rows = cur.fetchall()
        for row in rows:
                print(row)    
                print(row[0])
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()    

def main():
    createConnection(r"C:\SQLLite\Databases\COLUMBUS.db")

if __name__ == "__main__":
    main()
