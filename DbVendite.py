import sqlite3
import DbVendite
import DbClienti
import DbColli

# Questo modulo gestisce il database delle vendite in cantina e 
# verrà scritto solo in fase finale da  programma di gestione, non ci saranno
# scritture parziali, questo viene fatto per velocizzare il gestionale
# e evitare operazioni inutili.
#
# Importando questo modulo sarà possibile creare e gestire i seguenti database:
#   0) db_qualità  in questo database ci saranno tutte le qualità
#                   codice|nome esteso|anno|prezzo_sfuso|gradazione|prezzo_bot|prezzo_dama|prezzo_dama_noreso|codice_tasto
#                   Il codice è quello della qualità (BAR19 per esempio), ci sono poi i vari prezzi e l'anno, il nome esteso
#                   e quello che verrà scritto sullo scontrino
#   1) db_colli    ci sono tutti i tipi di collo:
#                   id|nome_collo|litri|cartonatura|tipo_prezzo|codice_tasto 
#                   dam54|damigiana|54|no|sfuso|12
#                   bot75|bottiglia|0.75|1,2,3,6,12|bot|13
#                   1,2,3,6,12 sono i cartoni possibli 
#                   
#   2) db_clienti   database dei clienti nel seguente formato:
#                   codice_fiscale|nome|cognome|regione|Provincia|Indirizzo|Età|sconti
#                   l'id è univoco per ciascun cliente
#
#   3) db_vendite   database dele vendite
#                   id_op|CF_cliente|n_operazione|data|ora|qualità|collo|quantità|cartonatura|prezzo_u|prezzo_t
#                   il CF_cliete è il codice fiscale dell'utente
#                   l'id_op è univoco per ciascuno scontrino, il numero di operazione è riferito al 
#                   numero di operazione all'interno dello scontrino, la cartonatura è un intero
#                   che indica il numero di cartoni per collo. Il prezzo_u = prezzo unitario
#                   c'è poi il prezzo totale prezzo_t


#################################################################################
# DB VENDITE    #################################################################
#################################################################################
# Questa classe gestisce il database delle vendite db_vendite.db
# in cui vengono salvate tutte le righe di ciascuno scontrino
# ogni scontrin ha un id_op e all'interno dello scontrino ciascuna vendita ha un 
# numero di operazione, esempio
# A1|RBLLEI96S19A182L|1|19-11-2020|18:30|BAR19|DAM54|0|1.80|97.2
# A1|RBLLEI96S19A182L|2|19-11-2020|18:30|BAR20|BOT075|3|6.5|19.5
# A1|RBLLEI96S19A182L|3|19-11-2020|18:30|BAR19|DAM34|0|1.80|61.2
# 
# Il nome dello scontrino è A1, per questo scontrino verranno salvati ulteriori dati
# nel database db_operazioni
# Quindi in generale
# id_op|CF_cliente|n_operazione|data|ora|qualità|collo|quantità|cartonatura|prezzo_u|prezzo_t
class DbVendite:
    def __init__(self, db_save_dir, csv_divider, db_clienti, db_qualità, db_colli):


    #############################################################################
    # IMPOSTARE  / CAMBIARE il database ########################################
    
    # Salva una nuova vendita
    def ImpostaNuovaVendita(self,id_op, CF_cliente, n_op, data, ora, qualita, collo, quantità, cartonatura, prezzo_u, prezzo_t):
    

    #############################################################################
    # LEGGERE dal database ######################################################

    # Esporta il database in csv
    def EsportaSuCSV(self, fp):

    # Da le info su una vendita effettuata dando l'id dello scontrino
    # se per quello scontrino sono state effettuate più vendite ritorna una 
    # lista di liste con una lista per ogni vendita
    def VenditaDaId(self, id_op):

        return lista_lista_vendite

    #############################################################################
    # Funzioni per gestire la creazione dello scontrino

    # Genera nuovo id che viene utilizzato poi per andare a crare delle nuove vendite
    # legate allo stesso scontrino, quando viene richiamato vengono abilitate le 
    # le funzioni che lavorano sullo scontrino ossia tutte quelle dopo
    def NewId(self):

        return id_op

    # Genera un nuovo numero di operazione , in questo modo le funzioni 
    # successive vengono abilitate a lavorare sulla suddedda operazione
    # L'operazione viene anche creata nel  database e vengono inizializzate:
    # Data e ora 
    def NewOp(self):
        # se si vuole creare una vendita che non sia la prima si deve aver 
        # eseguito almeno una volta la funzione Totale

        return n_op

    def ImpostaIdOp(self, id_op, n_op):


    def ImpostaLastIdOp(self):


    # Una volta che è stata chiamata NewId un nuovo scontrino viene generato, a 
    # questo punto bisogna generare una nuova operazione con NewOp.
    # Ora sarà possibile usare le funzioni successive che funzioneranno su
    # quello scontrino e quella operazione. 
    # Nel caso in cui si voglia modificare una vendita in uno scontrino
    # basterà chiamare ImpostaIdOp per far lavorare le funzioni successive su 
    # quella vendita.
    # Se si vuole poi ripristinare l'ultima vendita si chiama la funzione 
    # ImpostaLastIdOp

    # Quando la funzione NewId crea il nuovo id questo viene salvato internamente
    # e questa funzione viene abilitata,
    def ImpostaCFCliente(self, CF_cliente):


    def ImpostaQualita(self, qualità):

    def ImpostaCollo(self, collo):

        return cartonatura

    def ImpostaQuantita(self, quantita):

    def ImpostaCartonatura(self, cartonatura):

    # Impostando il prezzo unitario viene calcolato lo sconto 
    # e ritornato, viene già salvato nel database dei clienti
    def ImpostaPrezzoU(self, prezzo_u):

        return sconto

    def ImpostaPrezzoT(self, prezzo_t):

        return sconto

    # calcola il totale della vendita, lo salva nel database come prezzo_totale 
    # e lo ritorna, dopo questo si può fare ImpostaPrezzoT che lo risetta 
    # calcolando lo sconto.
    def Totale(self):
        
        return totale





