from array import array
# maior desceu que desceu da maria

import pandas as pd

df = pd.read_csv('exercicio1/pedrinhas.csv')

contagem = {'joao': 0, 'maria': 0}

contagem['joao'] = (df['classificacao'] == 1).sum() # joao
contagem['maria'] = (df['classificacao'] == 2).sum() # maria

numeros_distancia_joao = df['distancia'].to_list()

numeros_desceu_joao = df.loc[df['classificacao'] == 1, 'desceu']
media_desceu_joao = numeros_desceu_joao.sum() / contagem['joao']

numeros_desceu_maria = df.loc[df['classificacao'] == 2, 'desceu']
media_desceu_maria = numeros_desceu_maria.sum() / contagem['maria']

print(f"Temos {contagem['joao']} número 2 e {contagem['maria']} número 1")
print(f"média desceu joão = {media_desceu_joao}")
print(f"média desceu maria = {media_desceu_maria}")
