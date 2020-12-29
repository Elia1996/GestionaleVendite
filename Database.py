import sqlite3
import CSVData as csvd
import os


# https://riptutorial.com/it/python/example/14960/sqlite

class Database:

    def __init__(sf, db_save_dir, csv_divider):
        sf.db_name = "database.db"
        sf.save_dir = db_save_dir
        sf.csvd = csv_divider
        
        sf.conn = sqlite3.connect(sf.db_name)
        sf.cur = sf.conn.cursor()

        ##### Clienti 
        # verifica che nel database ci sia la tabella e crearla se non c'è
        sf.cur.execute("CREATE TABLE if not exists Clienti \
            ( id        INTEGER,\
              nome      TEXT,\
              cognome   TEXT,\
              CF        TEXT, \
              citta   TEXT, \
              provincia TEXT, \
              indirizzo TEXT, \
              CAP       TEXT,\
              PI        TEXT,\
              eta       INTEGER,\
              sconti    TEXT)")

        ##### Qualità
        # verifica che nel database ci sia la tabella e crearla se non c'è
        sf.cur.execute("CREATE TABLE if not exists Qualita \
                id                  INTEGER, \
                codice              TEXT, \
                nome                TEXT, \
                anno                INTEGER, \
                prezzo_sfuso        TEXT, \
                gradazione          INTEGER, \
                prezzo_bot          FLOAT, \
                prezzo dama         FLOAT, \
                prezzo_dama_noreso  FLOAT, \
                codice_tasto        INTEGER)")

        ##### Colli 
        # verifica ce nel database ci sia la tabella e crearla se non c'è

        ##### Vendite
        # verifica che nel database ci sia la tabella e crearla se non c'è
        sf.Commit()

        
    def Cursor(sf):
        sf.cur = sf.conn.cursor()

    def Commit(sf):
        sf.conn.commit()
    
    def Close(sf):
        sf.conn.close()
    
    def EraseDb(sf):
        sf.Close()
        os.remove(sf.db_name)
        sf.__init__(sf.save_dir, sf.csvd)
        
    #############################################################################
    # IMPOSTARE  / CAMBIARE  il database ########################################

    # Crea un nuovo id cliente non presente e lo ritorna
    def NuovoIdCliente(sf):
        sf.cur.execute("SELECT id FROM Clienti")
        data = sf.cur.fetchall()
        if len(data) == 0:
            return 0
        return max(data)[0]+1

    # Imposta un cliente nuovo oppure se l'id è già presente lo aggiorna
    # id_cliente, nome, cognome, CF, regione, provincia, indirizzo, eta, sconti
    def ImpostaCliente(sf, id_cliente, dz):
        # dz è un dizionario con elemento e valore da salvare
        # La lista sconti sarà del tipo:
        #   [id_qualità_id_collo_sconto_conto_percentuale]
        #   [BAR2019_BOT75_20]  sul barbera 2019 in bottiblia il 20% di sconto
        # Se gli sconti sono più di uno vengono appesi
        # BAR2019_BOT75_20-DOL2020_DAM54_10

        # If per sapere se il cliente è nuovo o meno
        header_clienti= sf.HeaderClienti()[1:]
        if int(id_cliente) in sf.IdClienti(): 
            print(sf.IdClienti())
            # aggiorno il cliente
            new_dz=[]
            for key in header_clienti:
                if key in dz:
                    # la key è presente nel dizionario passato e dev'essere quindi 
                    # modificato il valore corrispondente
                    new_dz.append(dz[key])
                else:
                    # La key  non viene data quindi si lascia immodificato il valore
                    query = """SELECT %s FROM Clienti WHERE id = %s""" % (key,id_cliente)
                    sf.cur.execute(query)
                    value=sf.cur.fetchall()[0]
                    print(value[0])
                    if value[0] == '':
                        new_dz.append("")
                        print(1)
                    else:
                        new_dz.append(value)
                        print(2)

            # Update dei valori
            toset=header_clienti[0]+"='"+new_dz[0]+"'"
            for head,value in zip(header_clienti[1:], new_dz[1:]):
                print(head,value)
                toset=toset+", "+head+"= '"+str(value)+"'"
            print(toset)
            query = """UPDATE Clienti set %s WHERE id = %s""" % (toset, id_cliente)
            print(query)

            sf.cur.execute(query)

        else:
            # creo un nuovo cliente
            new_dz=[]
            new_dz.append(id_cliente)
            # Ciclo sugli header e 
            for key in header_clienti:
                if not key in dz:
                    if key == 'eta':
                        new_dz.append(0)
                    else:
                        new_dz.append('')
                else:
                    new_dz.append(dz[key])
            
            # creazione del nuovo cliente
            toset="?"
            for i in header_clienti:
                toset=toset+", ?"
            query = """INSERT INTO Clienti VALUES (%s)""" % (toset)
            sf.cur.execute(query, new_dz)
        
        #sf.TabellaClienti() 
 
    
    #############################################################################
    # Importare esportare  il database ########################################

    # Permette di importare i clienti da un file CSV formattato con:
    #  id_cliente, nome, cognome, codice_fiscale, citta, Provincia, 
    #  Indirizzo,CAP, PI,  Età, sconto1, sconto2 ...
    def ImportaClientiDaCSV(sf, fp):
        [header, data] = csvd.clientiFromCSV(fp,sf.csvd)
        for cliente in data:
            dz = {}
            for h,c in zip(header[1:], cliente[1:]):
                dz[h]=c
            print(dz)
            sf.ImpostaCliente(cliente[0], dz)
        
        sf.TabellaClienti()
        return 0

    def EsportaClientiSuCSV(sf, fp):
            
        return 0

    #############################################################################
    # LEGGERE dal database ######################################################

    # Ritorna una tabella clienti 
    # id_cliente, nome, cognome, codice_fiscale, regione, Provincia, Indirizzo, Età, sconti
    def TabellaClienti(sf):
        sf.cur.execute("SELECT * FROM Clienti")
        tabella = sf.cur.fetchall()
        return tabella

    def HeaderClienti(sf):
        sf.cur.execute("SELECT * from Clienti")
        Header = [i[0] for i in sf.cur.description]
        return Header

    def IdClienti(sf):
        sf.cur.execute("SELECT id from Clienti")
        data = sf.cur.fetchall()
        id_list = [i[0] for i in data]
        return id_list
   
    def NomiCognomiClienti(sf):
        sf.cur.execute("SELECT nome , cognome from Clienti")    
        data=sf.cur.fetchall()
        return [' '.join(nc) for nc in data ]

    # Data una stringa ritorna un lista di "nomi cognomi" di clienti che
    # iniziano per quella stringa e una con i corrispettivi id_cliente
    def Stringa_Cliente(sf, s):
        stringa = s.lower()
        # lista dei clienti trovati che viene creata nel for
        l_c = []
        # ciclo sul nome_cognome dei clienti e sui loro id
        for nc_cliente, id_cliente in zip(sf.NomiCognomiClienti(),sf.IdClienti()):
                # toglo gli spazi e divido il nome-cognome in una lista
                l_nc = nc_cliente.strip().split(" ")
                # ciclo sulla lista per trovare i match
                for name in l_nc:
                    if stringa in name[0:len(stringa)].lower():
                        l_c.append([nc_cliente, id_cliente])
                        break
        return l_c  # [ [nome-cognome, id] [] [] ... ]

    # Ritorna lo sconto per un determinato cliente (da id del cliente) ed
    # un determinato lotto, il lotto viene formato unendo l'id della qualità e del collo
    # qualità BAR19, collo BOT75  -> lotto BAR19_BOT75
    # se lo sconto non è presente viene ritornato 0%
    def Cliente_Sconto(sf, id_cliente, id_qualità, id_collo):
        sconto=0
        return sconto

    # Se lo sconto del lotto dato è già presente lo aggiorna altrimenti lo crea
    def Cliente_ImpostaSconto(sf, id_cliente, lotto, sconto):

        return 0


