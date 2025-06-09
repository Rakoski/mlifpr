import pandas as pd
import numpy as np

def data_set(arquivo):
    resultado = {}
    resultado['nome-arquivo'] = arquivo

    data = pd.read_csv(arquivo, delimiter=";")

    cols = data.columns
    ultima = cols[-1]
    ph = data['pH']

    qualidade = data[ultima]

    qualidade_orig, cls_cnt = np.unique(qualidade, return_counts=True)

    resultado['qualidade-orig'] = qualidade_orig
    resultado['ph'] = ph.values
    resultado['cls-cnt'] = cls_cnt
    return resultado

data = data_set('./winequality-red.csv')

for key, value in data.items():
    print(f'{key} : {value}')

    ncls = len(data['cls-cnt'])
