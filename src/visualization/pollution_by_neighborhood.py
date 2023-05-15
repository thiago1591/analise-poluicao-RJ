import matplotlib.pyplot as plt
from IPython.display import display


def plotTopCo2Neighbordhood(df_media, limit):
    co2_mean = df_media.head(limit)
    plt.bar(co2_mean['NOME'], co2_mean['MEDIA_CO2'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO2')
    plt.title('Média total de CO2 por bairro')
    plt.savefig('reports/figures/topCo2Neighbordhood.png')
    
def plotTopCo2NeighbordhoodWeekend(df_media, limit):
    co2_mean = df_media.head(limit)
    plt.bar(co2_mean['NOME'], co2_mean['MEDIA_CO2'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO2')
    plt.title('Média total de CO2 por bairro no final de semana')
    plt.savefig('reports/figures/topCo2NeighbordhoodWeekend.png')

def plotTopCo2NeighbordhoodWeek(df_media, limit):
    co2_mean = df_media.head(limit)
    plt.bar(co2_mean['NOME'], co2_mean['MEDIA_CO2'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO2')
    plt.title('Média total de CO2 por bairro em dias úteis')
    plt.savefig('reports/figures/topCo2NeighbordhoodWeek.png')

def plotTopCo2NeighbordhoodCompareWeekAndWeekend(df_media_week, df_media_weekend, limit):
    df_media_week = df_media_week.head(limit)
    df_media_weekend = df_media_weekend.head(limit)
    coluna_comum = 'MEDIA_CO2'
    categorias = df_media_week[coluna_comum].unique()

    altura_df1 = df_media_week.groupby(coluna_comum).size()
    altura_df2 = df_media_weekend.groupby(coluna_comum).size()

    x = range(len(categorias))

    plt.bar(x, altura_df1, label='DataFrame 1')
    plt.bar(x, altura_df2, label='DataFrame 2')
    plt.xticks(x, categorias)
    plt.legend()
    plt.xlabel('Categorias')
    plt.ylabel('Contagem')
    plt.title('Comparação entre DataFrames')

def plotTopCoNeighbordhood(df_media, limit):
    co_mean = df_media.head(limit)
    plt.bar(co_mean['NOME'], co_mean['MEDIA_CO'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO')
    plt.title('Média total de CO por bairro')
    plt.savefig('reports/figures/topCoNeighbordhood.png')

def plotTopCoNeighbordhoodWeekend(df_media, limit):
    co_mean = df_media.head(limit)
    plt.bar(co_mean['NOME'], co_mean['MEDIA_CO'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO')
    plt.title('Média total de CO por bairro no final de semana')
    plt.savefig('reports/figures/topCoNeighbordhoodWeekend.png')

def plotTopCoNeighbordhoodWeek(df_media, limit):
    co2_mean = df_media.head(limit)
    plt.bar(co2_mean['NOME'], co2_mean['MEDIA_CO'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO')
    plt.title('Média total de CO por bairro em dias úteis')
    plt.savefig('reports/figures/topCONeighbordhoodWeek.png')

def plotTopNoxNeighbordhood(df_media, limit):
    nox_mean = df_media.head(limit)
    plt.bar(nox_mean['NOME'], nox_mean['MEDIA_NO_x'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de NOx')
    plt.title('Média total de NOx por bairro')
    plt.savefig('reports/figures/topNoXNeighbordhood.png')

def plotTopNoxNeighbordhoodWeekend(df_media, limit):
    nox_mean = df_media.head(limit)
    plt.bar(nox_mean['NOME'], nox_mean['MEDIA_NO_x'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de NOx')
    plt.title('Média total de NOx por bairro no final de semana')
    plt.savefig('reports/figures/topNOxNeighbordhoodWeekend.png')

def plotTopNoxNeighbordhoodWeek(df_media, limit):
    co2_mean = df_media.head(limit)
    plt.bar(co2_mean['NOME'], co2_mean['MEDIA_NOx'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de NOx')
    plt.title('Média total de NOx por bairro em dias úteis')
    plt.savefig('reports/figures/topNOxNeighbordhoodWeek.png')
