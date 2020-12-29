import sqlite
import os
# moduli miei
import CSVData as csvd

#################################################################################
# DB COLLI    ###################################################################
#################################################################################
# Questa classe imposta il database dei colli che ha i seguenti valori
# id|nome_collo|litri|cartonatura|tipo_prezzo|codice_tasto
class DbColli:
    def __init__(sf, db, csv_divider):
        sf.tb_name = "colli"
        sf.db = db
        sf.csv_div = csv_divider

        # Se il database è nuovo setto gli header
        if sf.db.total_changes == 0:
            sf.db.execute("CREATE TABLE ? 
                    (id_collo TEXT,
                     nome_collo TEXT,
                     litri FLOAT,
                     cartonatura INTEGER,
                     tipo_prezzo TEXT, 
                     codice_tasto TEXT)",
                     (sf.tb_name))


    #############################################################################
    # IMPOSTARE  / CAMBIARE  il database ########################################
    def Impos 
    # Permette di impostare un nuovo collo nel database
    def ImpostaNuovoCollo(sf, id_collo, nome_collo, litri, cartonatura, tipo_prezzo, codice_tasto):
        sf.last_id = id_collo
        sf.db.execute("INSERT INTO ? 
                    (id_collo ?,
                     nome_collo ?,
                     litri ?,
                     cartonatura ?,
                     tipo_prezzo ?, 
                     codice_tasto ?)", 
                     (sf.tb_name,
                      sf.last_id,
                      nome_collo, 
                      litri,
                      cartonatura,
                      tipo_prezzo,
                      codice_tasto))

    # Importa collo da csv file, se esiste già lo modifica
    def ImportaColliDaCSV(sf, fp):
        dati_csv=csvd.csvData(fp, sf.csv_div)
        if dati_scv[1] != sf.db.execute("SELECT * from bar")

    # Esporta database collo su csv per modifiche e reload
    def EsportaSuCSV(sf, fp):


    # Una volta che il database è completo se i tasti vogliono essere associati ad un altra
    # collo si può importare un file csv con codice nome_collo -> codice tasto
    def CambiaCodiciTasti_ColliCSV(sf, fp):

    # Permette di esportare su file solo "codice_tast collo" per essere modificati e riimportati
    def EsportaCodiciTasti_ColliSuCSV(sf, fp):
    
    
    #############################################################################
    # LEGGERE dal database ######################################################

    # Dando il codice del tasto vengono ritornati i dati cel collo
    def CodiceTasto_Proprieta(sf, codice_tasto):

        return [id_collo, nome_collo, litri ,cartonatura, tipo_prezzo]
    
