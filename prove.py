#!/usr/bin/env python3
import sqlite
import CSVData as csvd
import Database as database

db = database.Database('',';')
db.EraseDb()

#prova
if False:
    print(db.IdClienti())
    id_cliente = db.NuovoIdCliente()
    print(id_cliente)
    db.ImpostaCliente(id_cliente, {'nome':'ciccio', 'cognome':'seduto', 'CF':'RBLELERSEFEG10', 'regione':'Liguria', 'provincia':'GE', 'indirizzo':'Via della vacca 10', 'eta':22, 'sconti':'BAR19_BOT075_5'})
    id_cliente = db.NuovoIdCliente()
    print(id_cliente)
    db.ImpostaCliente(id_cliente, {'nome':'pluto', 'cognome':'seduto', 'CF':'RBLELERSEFEG10', 'regione':'Liguria', 'provincia':'GE', 'indirizzo':'Via della vacca 10', 'eta':22, 'sconti':'BAR19_BOT075_5'})
    id_cliente = db.NuovoIdCliente()
    print(id_cliente)
    db.ImpostaCliente(id_cliente, {'nome':'papero', 'cognome':'seduto', 'CF':'RBLELERSEFEG10', 'regione':'Liguria', 'provincia':'GE', 'indirizzo':'Via della vacca 10', 'eta':22, 'sconti':'BAR19_BOT075_5'})

    db.ImpostaCliente(1, {'nome':'ciccione', 'cognome':'seduto', 'CF':'RBLELERSEFEG10', 'regione':'Liguria', 'provincia':'GE', 'indirizzo':'Via della vacca 10', 'eta':213423, 'sconti':'BAR19_BOT075_5'})
    print(db.NomiCognomiClienti())

    print(db.Stringa_Cliente("pap"))
# ['id', 'name', 'cognome', 'indirizzo', 'CAP', 'citta', 'provincia', 'CF', 'PI']
elif True:
    db.ImportaClientiDaCSV("ElencoClientiO.csv")
    in_str=input()
    while in_str != "exit":
        print(db.Stringa_Cliente(in_str))
        in_str=input()
else:
    db.ImportaClientiDaCSV("ElencoClientiO.csv")
    print(db.NomiCognomiClienti())


db.Commit()
db.Close()

