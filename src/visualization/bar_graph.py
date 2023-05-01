import matplotlib.pyplot as plt

def plotCO2BarGraph(pollutionDfs):
    co2_by_neighborhood_df = pollutionDfs['co2_by_neighborhood_df']

    plt.bar(co2_by_neighborhood_df['CODBAIRRO'], co2_by_neighborhood_df['MEDIA_CO2'])
    plt.xlabel('ID do Bairro')
    plt.ylabel('gramas de CO2')
    plt.show()

def plotCOBarGraph(pollutionDfs):
    co_by_neighborhood_df = pollutionDfs['co_by_neighborhood_df']

    plt.bar(co_by_neighborhood_df['CODBAIRRO'], co_by_neighborhood_df['MEDIA_CO'])
    plt.xlabel('ID do Bairro')
    plt.ylabel('gramas de CO')
    plt.show()

def plotNoxBarGraph(pollutionDfs):
    nox_by_neighborhood_df = pollutionDfs['nox_by_neighborhood_df']

    plt.bar(nox_by_neighborhood_df['CODBAIRRO'], nox_by_neighborhood_df['MEDIA_NO_x'])
    plt.xlabel('ID do Bairro')
    plt.ylabel('gramas de NOx')
    plt.show()