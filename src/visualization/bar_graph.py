import matplotlib.pyplot as plt
from IPython.display import display
from src.features.neighborhoodsFromJson import *


def plotCO2BarGraph(pollutionDfs):
    co2_by_neighborhood_df = pollutionDfs['co2_by_neighborhood_df']
    co2_by_neighborhood_df = co2_by_neighborhood_df.sort_values(
        by='MEDIA_CO2', ascending=False)
    co2_by_neighborhood_df_10 = co2_by_neighborhood_df.head(10)

    dict = getNeighborhoodDict()

    #co2_by_neighborhood_df_10['NOME_BAIRRO'] = co2_by_neighborhood_df_10['CODBAIRRO'].map(dict)
    #not working yet

    plt.bar(co2_by_neighborhood_df_10['CODBAIRRO'],
            co2_by_neighborhood_df_10['MEDIA_CO2'])
    plt.xlabel('ID do Bairro')
    plt.ylabel('gramas de CO2')
    plt.show()


def plotCOBarGraph(pollutionDfs):
    co_by_neighborhood_df = pollutionDfs['co_by_neighborhood_df']

    plt.bar(co_by_neighborhood_df['CODBAIRRO'],
            co_by_neighborhood_df['MEDIA_CO'])
    plt.xlabel('ID do Bairro')
    plt.ylabel('gramas de CO')
    plt.show()


def plotNoxBarGraph(pollutionDfs):
    nox_by_neighborhood_df = pollutionDfs['nox_by_neighborhood_df']

    plt.bar(nox_by_neighborhood_df['CODBAIRRO'],
            nox_by_neighborhood_df['MEDIA_NO_x'])
    plt.xlabel('ID do Bairro')
    plt.ylabel('gramas de NOx')
    plt.show()
