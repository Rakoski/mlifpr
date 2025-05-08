from array import array
# maior desceu que desceu da maria

import pandas as pd

from array import array
# maior desceu que desceu da maria

import pandas as pd

df = pd.read_csv('exercicio1/pedrinhas.csv')

classificacao = df['classificacao']
pedrinha = df['desceu']
distancia = df['distancia']
contagem = {'joao': 0, 'maria': 0}
soma = {'joao': 0, 'maria': 0}

for cls, dsc in zip(classificacao, pedrinha):
    if cls == 1: key = 'joao'
    if cls == 2: key = 'maria'
    soma[key] = soma[key] + dsc
    contagem[key] += 1

media = {'joao': 0, 'maria': 0}
media['joao'] = soma['joao']/contagem['joao']
media['maria'] = soma['maria']/contagem['maria']
print(media)

soma_distancia = {'joao': 0, 'maria': 0}
contagem_distancia = {'joao': 0, 'maria': 0}

for dis, dsc in zip(classificacao, distancia):
    if dis == 1: key = 'joao'
    if dis == 2: key = 'maria'
    soma_distancia[key] = soma_distancia[key] + dsc
    contagem_distancia[key] += 1

media_distancia = {'joao': 0, 'maria': 0}
media_distancia['joao'] = soma_distancia['joao']/contagem_distancia['joao']
media_distancia['maria'] = soma_distancia['maria']/contagem_distancia['maria']
print(media_distancia)

# contagem['joao'] = (df['classificacao'] == 1).sum() # joao
# contagem['maria'] = (df['classificacao'] == 2).sum() # maria
#
# numeros_distancia_joao = df['distancia'].to_list()
#
# numeros_desceu_joao = df.loc[df['classificacao'] == 1, 'desceu']
# media_desceu_joao = numeros_desceu_joao.sum() / contagem['joao']
#
# numeros_desceu_maria = df.loc[df['classificacao'] == 2, 'desceu']
# media_desceu_maria = numeros_desceu_maria.sum() / contagem['maria']
#
# print(f"Temos {contagem['joao']} número 2 e {contagem['maria']} número 1")
# print(f"média desceu joão = {media_desceu_joao}")
# print(f"média desceu maria = {media_desceu_maria}")
