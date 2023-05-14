import matplotlib.pyplot as plt

def barGraphByDays(df_media):
    co2_mean = df_media['co2_mean'].head(3)
    plt.bar(co2_mean['NOME'], co2_mean['MEDIA_CO2'])
    plt.xlabel('Nome do Bairro')
    plt.ylabel('gramas de CO2')
    plt.title('Média total de CO2 por município (durante uma semana)')
    plt.show()