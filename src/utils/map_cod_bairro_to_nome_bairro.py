import pandas as pd

def addNeighborhoodName(dstB):
    counties = pd.read_csv('bairros.csv')[['NOME', 'CODBAIRRO']]
    neighborhoods = [ dstB[['ID', 'CODBAIRRO']] for dstB in dstB]
    neighborhoods = [neighborhood.dropna(subset=['CODBAIRRO']) for neighborhood in neighborhoods]
    neighborhoodsWithNames = [pd.merge(neighborhood.astype('int64'), counties, on='CODBAIRRO', how='left') for neighborhood in neighborhoods]
    dfs = [pd.merge(dstB[i], neighborhoodsWithNames[i], on='ID', how='left') for i in range(len(neighborhoodsWithNames))]
    return dfs