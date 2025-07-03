import pandas as pd
import numpy as np

# * Fazer uma função que retorne um dicionário contendo:
# * - uma chave do dataset (que vai ser o dataset inteiro já t, com exceção da coluna de classes)
# * - outra chave chamada classe (a coluna das classes já transformada em número)

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


def acabo_pro_betinha(dataset):
    result = {}

    data = dataset['data'].copy()

    classes = dataset['classes']

    cols = data.columns
    coluna_classe = cols[-2]

    dataset_sem_classes = data.drop(columns=[coluna_classe])

    result['dataset'] = dataset_sem_classes
    result['classe'] = classes

    return result


def calcular_desbalanceamento(cls_cnt):
    if len(cls_cnt) == 0:
        return 0

    max_count = np.max(cls_cnt)
    min_count = np.min(cls_cnt)

    if min_count == 0:
        return float('inf')

    desbalanceamento = max_count / min_count
    return desbalanceamento


FNAME = '../exercicio12/adult.csv'

if __name__ == '__main__':
    data = data_set(FNAME)
    print("resultadooo: ", data)
    print('-' * 40)

    print('nome-arquivo: ', data['nome-arquivo'])
    print(data['cls-orig'])
    print(data['cls-cnt'])
    print(data['classes'])
    ncls = len(data['cls-orig'])
    print(f'1 - possui {ncls} classes')
    print(f'2 - número de itens para cada classe: ', data['cls-cnt'])

    print("*" * 40)

    resultado = acabo_pro_betinha(data)
    print("Resultado da função acabo_pro_betinha:")
    print(f"Shape do dataset: {resultado['dataset'].shape}")
    print(f"Shape das classes: {resultado['classe'].shape}")
    print(f"Primeiras classes: {resultado['classe'][:10]}")

    print("*" * 40)

    soma = np.sum(data['cls-cnt'])
    result = []
    for vlr in data['cls-cnt']:
        result.append(soma / vlr)

    max_val = np.max(result)
    print("valor máximo: ", max_val)

    desbalanceamento = calcular_desbalanceamento(data['cls-cnt'])
    print(f"Desbalanceamento (maior/menor): {desbalanceamento:.2f}")