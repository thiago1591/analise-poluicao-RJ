import pandas as pd

def co2PerBusID(DSTs):
    neighborhood = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]

    co2 = [ dstE[['ID', 'CO_2']] for dstE in DSTs['dstE']]
    
    dstA = [ dstA[['ID', 'BUSID', 'LINE']] for dstA in DSTs['dstA']]

    dfs = [pd.merge(dstA[i], neighborhood[i], on='ID', how='left') for i in range(len(neighborhood))]
    dfs = [pd.merge(dfs[i], co2[i], on='ID', how='left') for i in range(len(co2))]
    
    dfs = [df.groupby('BUSID').mean(numeric_only=True).round() for df in dfs]
    dfs = [df.sort_values(by='CO_2', ascending=False) for df in dfs]
    
    dfs_concat = pd.concat(dfs)
    final_mean = dfs_concat.groupby('BUSID')['CO_2'].mean().reset_index()
    return final_mean

def coPerBusID(DSTs):
    neighborhood = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]

    co2 = [ dstE[['ID', 'CO']] for dstE in DSTs['dstE']]
    
    dstA = [ dstA[['ID', 'BUSID', 'LINE']] for dstA in DSTs['dstA']]

    dfs = [pd.merge(dstA[i], neighborhood[i], on='ID', how='left') for i in range(len(neighborhood))]
    dfs = [pd.merge(dfs[i], co2[i], on='ID', how='left') for i in range(len(co2))]
    
    dfs = [df.groupby('BUSID').mean(numeric_only=True).round() for df in dfs]
    dfs = [df.sort_values(by='CO', ascending=False) for df in dfs]
    
    dfs_concat = pd.concat(dfs)
    final_mean = dfs_concat.groupby('BUSID')['CO'].mean().reset_index()
    return final_mean

def noxPerBusID(DSTs):
    neighborhood = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]

    co2 = [ dstE[['ID', 'NO_x']] for dstE in DSTs['dstE']]
    
    dstA = [ dstA[['ID', 'BUSID', 'LINE']] for dstA in DSTs['dstA']]

    dfs = [pd.merge(dstA[i], neighborhood[i], on='ID', how='left') for i in range(len(neighborhood))]
    dfs = [pd.merge(dfs[i], co2[i], on='ID', how='left') for i in range(len(co2))]
    
    dfs = [df.groupby('BUSID').mean(numeric_only=True).round() for df in dfs]
    dfs = [df.sort_values(by='NO_x', ascending=False) for df in dfs]
    
    dfs_concat = pd.concat(dfs)
    final_mean = dfs_concat.groupby('BUSID')['NO_x'].mean().reset_index()
    return final_mean