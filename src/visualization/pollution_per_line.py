import matplotlib.pyplot as plt
from IPython.display import display


def plotCo2PerLine(df_media, limit):
    df = df_media.head(limit)
    plt.bar(df['LINE'], df['CO_2'])
    plt.xlabel('Linha')
    plt.ylabel('CO2 g/s')
    plt.title('Média de CO2 (g/s) por linha')
    plt.savefig('reports/figures/topCo2PerLine.png')

def plotCoPerLine(df_media, limit):
    df = df_media.head(limit)
    plt.bar(df['LINE'], df['CO'])
    plt.xlabel('Linha')
    plt.ylabel('CO g/s')
    plt.title('Média de CO (g/s) por linha')
    plt.savefig('reports/figures/topCoPerLine.png')

def plotNoxPerLine(df_media, limit):
    df = df_media.head(limit)
    plt.bar(df['LINE'], df['NO_x'])
    plt.xlabel('Linha')
    plt.ylabel('Nox g/s')
    plt.title('Média de Nox (g/s) por linha')
    plt.savefig('reports/figures/topNoxPerLine.png')