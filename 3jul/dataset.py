import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import numpy as np  # Importa a biblioteca numpy para operações numéricas


def _transform_col(data):
    #encontra valores únicos na coluna, retorna índices e contagens
    vlr_orig, values, count = np.unique(data, return_inverse=True, return_counts=True)

    result = {}  #cria um dicionário para armazenar os resultados
    result['vlr-orig'] = list(vlr_orig)  #armazena os valores originais únicos
    result['values'] = list(values)  #os índices dos valores únicos (encoding)
    result['vlr-count'] = list(count)  # a contagem de cada valor único
    return result  # dicionário com os resultados


def _transform_data(data, col_list):
    # percorre através de todas as colunas do DataFrame
    for colname in list(data.columns):
        if colname not in col_list: continue  #pula as colunas que não estão na lista especificada
        dados = data[colname]  #seleciona os dados da coluna atual
        ret = _transform_col(dados)  #aplica a transformação na coluna
        ret['colname'] = colname  #adiciona o nome da coluna ao resultado
        data.drop(
            columns=colname)  #remove a coluna original (NOTA: esta linha não tem efeito pois não salva o resultado)
        data[colname] = ret['values']  #substitui os dados originais pelos valores codificados

    return data  #retorna o DataFrame transformado


def dataset_info(data):
    data.info(verbose=True)  #mostra informações detalhadas sobre o DataFrame
    print(data.describe())  #mostra estatísticas descritivas dos dados
    print('tipos:', data.dtypes)  #mostra os tipos de dados de cada coluna
    print('dimensoes:', data.ndim)  #mostra o número de dimensões do DataFrame
    print('linhas x colunas:', data.shape)  #mostra o número de linhas e colunas


def remover_dados_faltantes(df):
    #cria uma máscara para identificar linhas que contêm '?' em qualquer coluna
    mascara = df.apply(lambda linha: linha.astype(str).str.contains(r'\?')).any(axis=1)

    #retorna um DataFrame apenas com as linhas que **não** contêm '?'
    data = df[~mascara].copy()  #usa o operador ~ para inverter a máscara e .copy() para criar uma cópia
    return data  #retorna o DataFrame limpo


def data_set(fname):
    result = {}  #cria um dicionário para armazenar os resultados
    result['nome-arquivo'] = fname  #armazena o nome do arquivo

    #lê o arquivo CSV removendo espaços extras e linhas em branco
    data = pd.read_csv(fname, skipinitialspace=True, skip_blank_lines=True)
    dataset_info(data)  #mostra informações do dataset original

    data = remover_dados_faltantes(data)  #remove linhas com dados faltantes (marcados com '?')
    # data.to_csv('adult--removido.csv', index=False)  #linha comentada que salvaria o dataset limpo
    dataset_info(data)  #mostra informações do dataset após remoção de dados faltantes

    #define as colunas categóricas que precisam ser transformadas
    mystr = 'workclass, education,  marital-status, occupation,     relationship,   race,   sex,    native-country, class'
    process = [x.strip() for x in mystr.split(',')]  #cria uma lista removendo espaços extras
    data = _transform_data(data, process)  #aplica a transformação (encoding) nas colunas categóricas

    ultima = data.columns[-1]  #pega o nome da última coluna (variável target)
    classes = list(data[ultima])  #extrai os valores da coluna de classes
    df = data.drop(columns=ultima)  # Remove a coluna de classes dos dados de features

    result['dados'] = df  # Armazena as features no resultado
    result['classes'] = classes  # Armazena as classes no resultado

    return result  # Retorna o dicionário com dados e classes separados

import pandas as pd  # Importa pandas novamente (redundante)
import numpy as np  # Importa numpy novamente (redundante)

def split_and_save_dataset(data, test_size=0.2, random_state=42):
    # pegando os dados
    X = data['dados']  # Extrai as features do dicionário
    y = data['classes']  # Extrai as classes do dicionário

    # pega todas as amostras
    n_samples = len(X)  # Calcula o número total de amostras
    n_test = int(n_samples * test_size)  # Calcula o número de amostras para teste
    n_train = n_samples - n_test  # Calcula o número de amostras para treino

    # coloca seed aleatória pra depois poder reproduzir tbm
    np.random.seed(random_state)

    #indices aleatorios
    indices = np.random.permutation(n_samples)  # Gera uma permutação aleatória dos índices

    # Split desses indices
    train_indices = indices[:n_train]  #seleciona os índices para treino
    test_indices = indices[n_train:]  #seleciona os índices para teste

    # Split de features (X)
    X_train = X.iloc[train_indices]  #seleciona as features de treino usando os índices
    X_test = X.iloc[test_indices]  #seleciona as features de teste usando os índices

    # Split do target (y)
    y_train = [y[i] for i in train_indices]  #seleciona as classes de treino usando os índices
    y_test = [y[i] for i in test_indices]  #seleciona as classes de teste usando os índices

    # salvando p csv
    X_train.to_csv('xtreino.csv', index=False)  # Salva as features de treino em CSV
    X_test.to_csv('xteste.csv', index=False)  # Salva as features de teste em CSV

    # salando os dados y
    pd.DataFrame(y_train, columns=['class']).to_csv('ytreino.csv', index=False)  # Salva as classes de treino
    pd.DataFrame(y_test, columns=['class']).to_csv('yteste.csv', index=False)  # Salva as classes de teste

    # Imprime informações sobre a divisão dos dados
    print(f"Dataset split and saved:")
    print(f"  Total samples: {n_samples}")  #mostra o total de amostras
    print(f"  Training samples: {n_train} ({(n_train / n_samples) * 100:.1f}%)")  #,ostra amostras de treino
    print(f"  Test samples: {n_test} ({(n_test / n_samples) * 100:.1f}%)")  #mostra amostras de teste
    print(f"  Files saved: xtreino.csv, xteste.csv, ytreino.csv, yteste.csv")  #lista os arquivos salvos