import pandas as pd

def timePerOneNeighborhood(DSTs, neighborhoodName):
    dstB = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]
    intervals = [ dstD[['ID', 'INTERVAL']] for dstD in DSTs['dstD']]

    dfs = [pd.merge(dstB[i], intervals[i], on='ID', how='left') for i in range(len(intervals))]

    for df in dfs:
        df['INTERVAL'] = df['INTERVAL'].dt.total_seconds()

    dataframes_filtrados = [] 

    for df in dfs:
        df_filtrado = df[df['NOME'] == neighborhoodName]
        dataframes_filtrados.append(df_filtrado)

    df_final = pd.concat(dataframes_filtrados)
    seconds = df_final['INTERVAL'].sum()
    hours = int((seconds/60/60).round())
    return hours