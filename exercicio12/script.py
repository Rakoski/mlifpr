import pandas as pd
import numpy as np

def data_set(aname):
    result = {}
    result['nome-arquivo'] = aname
    data = pd.read_csv(aname)

    data = data.map(lambda x: x.strip() if isinstance(x, str) else x)

    data = data[~data.isin(['?']).any(axis=1)]
    data = data.dropna()

    idade_col = 'vl1'

    bins = [0, 17, 29, 44, 59, 100]
    labels = ['jovem', 'jovem-adulto', 'adulto', 'meia-idade', 'idoso']
    data['idade_faixa'] = pd.cut(data[idade_col].astype(int), bins=bins, labels=labels, right=True)

    for col in data.columns:
        if data[col].dtype == 'object' or str(data[col].dtype).startswith('category'):
            data[col], _ = pd.factorize(data[col])

    cols = data.columns
    ultima = cols[-2]
    nome_orig = data[ultima]

    cls_orig, classes, cls_cnt = np.unique(nome_orig, return_inverse=True, return_counts=True)

    print("classes 1: ", classes)

    result['classes'] = classes
    result['cls-orig'] = cls_orig
    result['cls-cnt'] = cls_cnt
    result['data'] = data

    return result
FNAME = './adult.csv'
#
# with open(fname, 'r') as file:
#     tmp = np.loadtxt(file)
#     print(tmp)

if __name__ == '__main__':
    data = data_set(FNAME)
    print('-' * 40)

    for key, value in data.items():
        print(f'{key} : {value}')

    print('nome-arquivo: ', data['nome-arquivo'])
    print(data['cls-orig'])
    print(data['cls-cnt'])
    print(data['classes'])
    ncls = len(data['cls-orig'])
    print(f'1 - possui {ncls} classes')
    print(f'2 - número de itens  para cada classe: ', data['cls-cnt'])

    print("*" * 40)
    soma = np.sum(data['cls-cnt'])
    result = []
    for vlr in data['cls-cnt']:
        result.append(soma / vlr)

    max = np.max(result)
    print("valor máximo: ", max)

# DESBALANCEAMENTO -> CALCULAR EM UMA LISTA QUAL O MAIOR VALOR E O MENOR VALOR, PEGA O ÍNDICE (MAIOR VALOR / MENOR VALOR)
# 0 - 10 -> 10/45 -> 2 MAX
# 1 - 15 -> 15/45 -> 3 MAX
# 2 - 20 -> 20/45 -> 4 MAX
# =======> total -> 45 -> 4

# Datasets para treinar ML
# NUMERO INSTANCIAS -> NUMERO LINHAS
# FEATURES -> NÚMERO DE COLUNAS (DIMENSÃO)
# ↦ UCI Machine Learning Repository
# ↦ Kaggle
# ↦ Google Dataset Search
# ↦ Data.gov
# ↦ Open Data Network
# ↦ World Bank Open Data
#
# https://archive.ics.uci.edu/ml/index.php
#
# https://www.kaggle.com/
#
# https://datasetsearch.research.google.com/
#
# https://www.opendatanetwork.com/
#
# https://data.worldbank.org/