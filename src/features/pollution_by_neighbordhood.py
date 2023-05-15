import pandas as pd
import numpy as np

def pollutionByNeighbordhood(DSTs):
    intervals = [ dstD[['ID', 'INTERVAL']] for dstD in DSTs['dstD']]
    neighborhood = [ dstB[['ID', 'NOME']] for dstB in DSTs['dstB']]

    dfs = [pd.merge(DSTs['dstE'][i], intervals[i], on='ID', how='left') for i in range(len(intervals))]
    dfs = [pd.merge(dfs[i], neighborhood[i], on='ID', how='left') for i in range(len(neighborhood))]

    for df in dfs:
        df['INTERVAL'] = df['INTERVAL'].dt.total_seconds()

    for df in dfs:
        df['CO2_total'] = np.multiply(df['CO_2'], df['INTERVAL'])
        df['CO_total'] = np.multiply(df['CO'], df['INTERVAL'])
        df['NO_x_total'] = np.multiply(df['NO_x'], df['INTERVAL'])

    df_co2s = [df.loc[:, ['ID', 'NOME', 'CO2_total']] for df in dfs]
    df_cos = [df.loc[:, ['ID', 'NOME', 'CO_total']] for df in dfs]
    df_noxs = [df.loc[:, ['ID', 'NOME', 'NO_x_total']] for df in dfs]

    df_co2_medias = [df_co2.groupby('NOME').sum(numeric_only=True) for df_co2 in df_co2s]

    for i in range(len(df_co2_medias)):
        df_co2_medias[i] = df_co2_medias[i].rename(columns={'CO2_total': 'MEDIA_CO2'})
        df_co2_medias[i] = df_co2_medias[i].reset_index()

    df_co_medias = [df_co.groupby('NOME').sum(numeric_only=True) for df_co in df_cos]

    for i in range(len(df_co_medias)):
        df_co_medias[i] = df_co_medias[i].rename(columns={'CO_total': 'MEDIA_CO'})
        df_co_medias[i] = df_co_medias[i].reset_index()

    df_nox_medias = [df_co.groupby('NOME').sum(numeric_only=True) for df_co in df_noxs]

    for i in range(len(df_nox_medias)):
        df_nox_medias[i] = df_nox_medias[i].rename(columns={'NO_x_total': 'MEDIA_NO_x'})
        df_nox_medias[i] = df_nox_medias[i].reset_index()
    
    co2_concatenado = pd.concat(df_co2_medias)
    co_concatenado = pd.concat(df_co_medias)
    nox_concatenado = pd.concat(df_nox_medias)

    co2_final_mean = co2_concatenado.groupby('NOME')['MEDIA_CO2'].mean().reset_index()
    co_final_mean = co_concatenado.groupby('NOME')['MEDIA_CO'].mean().reset_index()
    nox_final_mean = nox_concatenado.groupby('NOME')['MEDIA_NO_x'].mean().reset_index()

    co2_final_mean = co2_final_mean.sort_values(by='MEDIA_CO2', ascending=False)
    co_final_mean = co_final_mean.sort_values(by='MEDIA_CO', ascending=False)
    nox_final_mean = nox_final_mean.sort_values(by='MEDIA_NO_x', ascending=False)
    
    return {
        "co2_mean": co2_final_mean,
        "co_mean": co_final_mean,
        "nox_mean": nox_final_mean
    }