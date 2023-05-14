import pandas as pd

def registersByNeighborhood(DSTs, neighborhoodName):
    neighborhood = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]

    dataframes_filtrados = []

    for df in neighborhood:
        df_filtrado = df[df['NOME'] == neighborhoodName]
        dataframes_filtrados.append(df_filtrado)

    return len(pd.concat(dataframes_filtrados))