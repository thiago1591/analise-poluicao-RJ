import pandas as pd

def timePerNeighborhood(DSTs):
    dstB = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]
    intervals = [ dstD[['ID', 'INTERVAL']] for dstD in DSTs['dstD']]

    dfs = [pd.merge(dstB[i], intervals[i], on='ID', how='left') for i in range(len(intervals))]

    for df in dfs:
        df['INTERVAL'] = (df['INTERVAL'].dt.total_seconds())

    df_somas = []
    for i, df in enumerate(dfs):
        df_soma = df.groupby('NOME')['INTERVAL'].sum().reset_index()
        df_soma['day'] = f'day {i+1}'
        df_somas.append(df_soma)
    
    df_concat = pd.concat(df_somas)

    df_media = df_concat.groupby('NOME')['INTERVAL'].mean().reset_index()

    # df_final = pd.concat(dfs)
    # df_final = df_final.groupby('NOME')['INTERVAL'].mean().reset_index()
    df_media = df_media.sort_values(by='INTERVAL', ascending=False)

    return df_media