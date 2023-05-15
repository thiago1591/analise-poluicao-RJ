import matplotlib.pyplot as plt
from IPython.display import display


def plotCo2PerLine(df_media, limit):
    df = df_media.head(limit)
    plt.bar(df['LINE'], df['CO_2'])
    plt.xlabel('Linha')
    plt.ylabel('CO2 g/s')
    plt.title('Média de CO2 (g/s) por linha')
    plt.savefig('reports/figures/topCo2PerLine.png')
    plt.show()