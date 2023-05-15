import pandas as pd

def co2PerLine(DSTs):
    neighborhood = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]
    co2 = [ dstE[['ID', 'CO_2']] for dstE in DSTs['dstE']]
    
    dstA = [ dstA[['ID', 'BUSID', 'LINE']] for dstA in DSTs['dstA']]

    dfs = [pd.merge(dstA[i], neighborhood[i], on='ID', how='left') for i in range(len(neighborhood))]
    dfs = [pd.merge(dfs[i], co2[i], on='ID', how='left') for i in range(len(co2))]
    
    dfs = [df.groupby('LINE').mean(numeric_only=True).round() for df in dfs]
    dfs = [df.sort_values(by='CO_2', ascending=False) for df in dfs]
    
    dfs_concat = pd.concat(dfs)
    final_mean = dfs_concat.groupby('LINE')['CO_2'].mean().reset_index()
    final_mean = final_mean.sort_values(by='CO_2', ascending=False)
    return final_mean
    