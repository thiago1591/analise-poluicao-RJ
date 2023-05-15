import matplotlib.pyplot as plt
from IPython.display import display


def plotTimePerNeighborhood(df_media, limit):
    df = df_media.head(limit)
    plt.bar(df['NOME'], df['INTERVAL'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO2')
    plt.title('Média total de CO2 por bairro em')