#!/usr/bin/env python3

import sqlite3

# create if don't exist
conn = sqlite3.connect("database.db")

print(conn.total_changes)

cursor = conn.cursor()
#cursor.execute("CREATE TABLE if not exists Pippo ( id TEXT , n_operazione INTEGER, data TEXT, prezzo_totale FLOAT)")
#cursor.execute("INSERT INTO Pippo VALUES ('c0', 10, 'daafa', 78.00)")
#cursor.execute("INSERT INTO Pippo VALUES ('c1', 1, 'dewqraafa', 79.00)")
#cursor.execute("INSERT INTO Pippo VALUES ('c2', 101, 'dawewrafa', 74.00)")
cursor.execute("INSERT INTO Pippo VALUES (?, ?, 'daafeea', 71.00)", ['dd',1])
#cursor.execute("SELECT n_operazione FROM Pippo WHERE id = 'c1'")
dz={'id':'cc', 'n_operazione':20, 'data':'arfgas','prezzo_totale':1.34}
for key in dz.keys():
    print(key, dz[key])

cursor.execute("select * from Pippo")
print(cursor.fetchall())
conn.commit()
conn.close()
#cursor.execute(
#        "UPDATE tb_name SET litri = 54 WHERE id = c1"        
#)

