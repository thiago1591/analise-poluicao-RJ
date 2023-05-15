import matplotlib.pyplot as plt
from IPython.display import display


def plotCo2PerBus(df_media, limit):
    df = df_media.head(limit)
    plt.bar(df['BUSID'], df['CO_2'])
    plt.xlabel('ID do Ônibus')
    plt.ylabel('CO2 g/s')
    plt.title('Média de CO2 (g/s) por ônibus')
    plt.savefig('reports/figures/topCo2PerBus.png')