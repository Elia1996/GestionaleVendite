import pandas as pd
import os.path 


def csvData(filename, divider):
        if os.path.isfile(filename):
            df = pd.read_csv(filename, sep=divider, engine='python', header=None)
            data = df.values.tolist()
            # Uses the first row (which should be column names) as columns names
            table_header = df.iloc[0].tolist()
            #[var.replace('_',' ') for var in df.iloc[0].tolist()]
            # Drops the first row in the table i
            # (otherwise the header names and the first row will be the same)
            data = df[1:].values.tolist()
        else:
            data=[]
            table_header=[]
        return [data,table_header]

def clientiFromCSV(filename, divider):
    [data,header]=csvData(filename, divider)
    lista_clienti=[]
    for nc in data:
        list_nc=nc[1].split(' ')
        lista_nc=[list_nc[0], ' '.join(list_nc[1:])]
        lista_clienti.append([nc[0]] + lista_nc + nc[2:])

    new_header =[ header[0] ]+ [ 'nome', 'cognome' ] + header[2:]
    return [new_header, lista_clienti]

        
