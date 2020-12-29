import sqlite

#################################################################################
# DB QUALITA'  ##################################################################
#################################################################################
# Questa classe fornisce il primo livello di interfaccia del database db_qualità, permette
# di creare nuove qualita, ogni qualità è collegata ad un codice di tasto e ad un prezzo per
# ogni tipo di collo, sono salvate anche altre caratteristiche del vino.
# database db_qualita.db
class DbQualita:

    def __init__(self, db_save_dir, csv_divider):
        # Creo il database se non esiste immettendo gli header corretti

    #############################################################################
    # IMPOSTARE  / CAMBIARE  il database ########################################

    # Imposta nuova qualità sul database
    def ImpostaNuovaQualita(self, codice, nome_esteso, anno, prezzo_sfuso, gradazione, prezzo_bot, prezzo dama, prezzo_dama_noreso, codice_tasto):


    # Permette di importare da csv le qualità
    # Ogni riga del file csv sarà una riga di database
    # Se la qualità esiste già viene sovrascritta
    def ImportaQualitaDaCSV(self, fp):


    # Permette di esportare il database delle qualità su CSV per essere modificata e ricaricata
    def EsportaSuCSV(self, fp):

    # Una volta che il database è completo se i tasti vogliono essere associati ad un altra
    # qualità si può importare un file csv con codice qualità -> codice tasto
    def CambiaCodiciTasti_QualitaCSV(self, fp):


    # Esporta "codice_tasto, qualità" su file, li divisore è quello indicato nell'init
    def EsportaCodiciTasti_QualitaSuCSV(self, fp):


    #############################################################################
    # LEGGERE dal database ######################################################

    # Dando il codice del tasto vengono ritornati : il nome esteso, l'anno e la
    # gradazione del vino
    def CodiceTasto_Proprieta(self, codice):

        return [nome_esteso, anno, gradazione]

    # Dando il codice del tasto e il tipo di collo viene ritornato il prezzo unitario
    #   codice=BAR19 , tipo=sfuso - > viene dato il prezzo al litro sfuso
    def CodiceTastoTipo_Prezzo(self, codice, tipo):

        return [prezzo]


