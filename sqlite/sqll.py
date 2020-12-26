#!/usr/bin/env python3

import sqlite3

# create if don't exist
conn = sqlite3.connect("acqua.db")

print(conn.total_changes)

cursor = conn.cursor()
cursor.execute("CREATE TABLE ? (id TEXT ,n_operazione INTEGER, data TEXT, qualità TEXT qualità TEXT, collo TEXT, quantità INTEGER, prezzo_unitario FLOAT, prezzo_totale FLOAT)", ("Pippo"))
cursor.execute("INSERT INTO acquisto VALUES ('Barbera', 'Bottiglie 0.75l', 12, 6.50, 78.00)")
cursor.execute("SELECT qualità FROM acquisto")
print(cursor.fetchall())
cursor.execute(
    "UPDATE ? SET qualità = ? WHERE "        
)

