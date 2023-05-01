import pandas as pd
import numpy as np

def findPollutionByNeighborhood(DSTs):
    dst0, dstA, dstB, dstC, dstD, dstE = DSTs.values()

    # merge dos DSTs
    interval = dstD[['ID', 'INTERVAL']]
    neighborhood = dstB[['ID', 'CODBAIRRO']]
    df = pd.merge(dstE, interval, on='ID', how='left')
    df = pd.merge(df, neighborhood, on='ID', how='left')
    df['INTERVAL'] = df['INTERVAL'].dt.total_seconds()

    # calcular poluicao
    df['CO2_total'] = np.multiply(df['CO_2'], df['INTERVAL'])
    df['CO_total'] = np.multiply(df['CO'], df['INTERVAL'])
    df['NO_x_total'] = np.multiply(df['NO_x'], df['INTERVAL'])

    # sub datasets
    df_co2 = df.loc[:, ['ID', 'CODBAIRRO', 'CO2_total']]
    df_co = df.loc[:, ['ID', 'CODBAIRRO', 'CO_total']]
    df_nox = df.loc[:, ['ID', 'CODBAIRRO', 'NO_x_total']]

    # calculando media
    df_co2_media = df_co2.groupby('CODBAIRRO').mean().round()
    df_co2_media = df_co2_media.rename(columns={'CO2_total': 'MEDIA_CO2'})
    df_co2_media = df_co2_media.reset_index()

    df_co_media = df_co.groupby('CODBAIRRO').mean().round()
    df_co_media = df_co_media.rename(columns={'CO_total': 'MEDIA_CO'})
    df_co_media = df_co_media.reset_index()

    df_nox_media = df_nox.groupby('CODBAIRRO').mean().round()
    df_nox_media = df_nox_media.rename(columns={'NO_x_total': 'MEDIA_NO_x'})
    df_nox_media = df_nox_media.reset_index()

    return {
        "co2_by_neighborhood_df": df_co2_media,
        "co_by_neighborhood_df": df_co_media,
        "nox_by_neighborhood_df": df_nox_media,
    }