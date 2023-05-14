import pandas as pd

def co2PerLine(DSTs):
    counties = pd.read_csv('bairros.csv')[['NOME', 'CODBAIRRO']]
    neighborhoods = [ dstB[['ID', 'CODBAIRRO']] for dstB in DSTs['dstB']]
    neighborhoods = [neighborhood.dropna(subset=['CODBAIRRO']) for neighborhood in neighborhoods]

    co2 = [ dstE[['ID', 'CO_2']] for dstE in DSTs['dstE']]
    
    dstA = [ dstA[['ID', 'BUSID', 'LINE']] for dstA in DSTs['dstA']]

    neighborhoodsWithNames = [pd.merge(neighborhood.astype('int64'), counties, on='CODBAIRRO', how='left') for neighborhood in neighborhoods]
    dfs = [pd.merge(dstA[i], neighborhoodsWithNames[i], on='ID', how='left') for i in range(len(neighborhoodsWithNames))]
    dfs = [pd.merge(dfs[i], co2[i], on='ID', how='left') for i in range(len(co2))]
    
    dfs = [df.groupby('LINE').mean(numeric_only=True).round() for df in dfs]
    dfs = [df.sort_values(by='CO_2', ascending=False) for df in dfs]
    
    dfs_concat = pd.concat(dfs)
    final_mean = dfs_concat.groupby('LINE')['CO_2'].mean().reset_index()
    return final_mean
    