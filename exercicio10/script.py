import pandas as pd
import numpy as np

def data_set(aname):
    result = {}
    result['nome-arquivo'] = aname
    data = pd.read_csv(aname)
    cols = data.columns
    ultima = cols[-1]

    nome_orig = data[ultima]
    cls_orig, classes = np.unique(nome_orig, return_inverse=True)

    print("classes 1: ", classes)

    df = data.drop(columns=ultima)

    print("ultima: ", ultima)
    print("df: ", df)

    result['dados'] = df

    return result

FNAME = '../exercicio9/iris.csv'
#
# with open(fname, 'r') as file:
#     tmp = np.loadtxt(file)
#     print(tmp)

if __name__ == '__main__':
    data = data_set(FNAME)
    print('-' * 40)
    print('nome-arquivo: ', data['nome-arquivo'])