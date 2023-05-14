import pandas as pd

def busIDByNeighbordhood(DSTs, neighborhoodName):
    neighborhood = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]
    co2 = [ dstE[['ID', 'CO_2']] for dstE in DSTs['dstE']]
    dstA = [ dstA[['ID', 'BUSID', 'LINE']] for dstA in DSTs['dstA']]

    dfs = [pd.merge(dstA[i], neighborhood[i], on='ID', how='left') for i in range(len(neighborhood))]
    dfs = [pd.merge(dfs[i], co2[i], on='ID', how='left') for i in range(len(co2))]
    dfs = [df.dropna(subset=['NOME']) for df in dfs]
    dataframes_filtrados = []

    for df in dfs:
        df_filtrado = df[df['NOME'] == neighborhoodName]
        dataframes_filtrados.append(df_filtrado)

    df_final = pd.concat(dataframes_filtrados).groupby('BUSID').first().reset_index()

    #media do valor de co2 g/s dos onibus que passam pelo bairro:
    media = df_final['CO_2'].mean()

    #numero de onibus que passam pelo bairro:
    num = len(df_final)
    return num
