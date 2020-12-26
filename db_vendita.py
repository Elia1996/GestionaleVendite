import sqlite3

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
#                   nome_collo|litri|cartonatura|tipo_prezzo|codice_tasto 
#                   damigiana|54|no|sfuso|12
#                   bottiglia|0.75|1,2,3,6,12|bot|13
#                   1,2,3,6,12 sono i cartoni possibli 
#                   
#   2) db_clienti   database dei clienti nel seguente formato:
#                   id_cliente|nome|cognome|codice fiscale|regione|Provincia|Indirizzo|Età|sconti
#                   l'id è univoco per ciascun cliente
#
#   3) db_vendite   database dele vendite
#                   id_op|id_cliente|n_operazione|data|qualità|collo|quantità|cartonatura|prezzo_u|prezzo_t
#                   l'id_op è univoco per ciascuno scontrino, il numero di operazione è riferito al 
#                   numero di operazione all'interno dello scontrino, la cartonatura è un intero
#                   che indica il numero di cartoni per collo. Il prezzo_u = prezzo unitario
#                   c'è poi il prezzo totale prezzo_t
#   4) db_operazioni   database con una riga per ciascuno scontrino, ogni scontrino ha l'id_operazione univoco
#                   id_operazione|totale|
class Db_Qualita:
    def __init__(self, save_dir):
        # Creo il database se non esiste immettendo gli header corretti

    def GuiImpostaNuovaQualita(self):


    def GuiCambiaQualita(self):


    def ImportaNuoveQualitaDaCSV(self, filename):


    def ImportaQualitaDaCSV(self, filename):



    def CodiceTasto_Proprieta(self, codice):

        return [codice, nome_esteso, anno, gradazione]

    def CodiceTastoTipo_Prezzo(self, codice, tipo):
        
        return [prezzo]

    


    





