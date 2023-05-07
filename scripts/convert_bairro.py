import pandas as pd

df = pd.read_csv('Limite_de_Bairros.csv')
newdf = df[['NOME', 'CODBAIRRO']]
dfJson = newdf.to_json('bairros.json', orient='records',
                       force_ascii=False)
