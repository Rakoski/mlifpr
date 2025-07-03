import pandas as pd
import numpy as np


def _transform_col(data):
    vlr_orig, values, count = np.unique(data, return_inverse=True, return_counts=True)
    result = {}
    result['vlr-orig'] = list(vlr_orig)
    result['values'] = list(values)
    result['vlr-count'] = list(count)
    return result


def _transform_data(data, col_list):
    for colname in list(data.columns):
        if colname not in col_list:
            continue
        dados = data[colname]
        ret = _transform_col(dados)
        ret['colname'] = colname
        data[colname] = ret['values']
    return data


def dataset_info(data):
    print("=== INFORMAÇÕES DO DATASET ===")
    data.info(verbose=True)
    print("\n=== ESTATÍSTICAS DESCRITIVAS ===")


def remove_invalid_numbers(data):
    print("\n=== REMOVENDO VALORES INVÁLIDOS ===")

    question_marks = (data == '?').sum().sum()
    print(f"Total de '?' encontrados: {question_marks}")

    data = data.replace('?', np.nan)

    missing_cols = data.isnull().sum()
    missing_cols = missing_cols[missing_cols > 0]
    if len(missing_cols) > 0:
        print("Colunas com valores faltantes:")
        for col, count in missing_cols.items():
            print(f"  {col}: {count} valores faltantes")

    data_clean = data.dropna()

    for col in data.columns:
        if data[col].isnull().any():
            if data[col].dtype == 'object':  # Coluna categórica
                mode_value = data[col].mode()
                if len(mode_value) > 0:
                    data[col].fillna(mode_value[0], inplace=True)
            else:
                median_value = data[col].median()
                data[col].fillna(median_value, inplace=True)

    print(f"Dataset limpo. Valores faltantes restantes: {data.isnull().sum().sum()}")
    return data


def convert_target_to_binary(target_column):
    """
    Convert target classes to binary encoding directly from string values
    0 = <=50K, 1 = >50K
    """
    print("\n=== CONVERTENDO TARGET PARA BINÁRIO ===")

    # Create binary mapping directly from string values
    binary_classes = []
    for class_value in target_column:
        if class_value == '<=50K':
            binary_classes.append(0)
        elif class_value == '>50K':
            binary_classes.append(1)
        else:
            print(f"Valor inesperado encontrado: {class_value}")
            binary_classes.append(-1)  # Flag unexpected values

    # Count the distribution
    unique_values, counts = np.unique(binary_classes, return_counts=True)
    print("Distribuição das classes binárias:")
    for val, count in zip(unique_values, counts):
        if val == 0:
            print(f"  {val} (<=50K): {count} amostras")
        elif val == 1:
            print(f"  {val} (>50K): {count} amostras")
        else:
            print(f"  {val} (valor inesperado): {count} amostras")

    return binary_classes


def data_set(fname):
    """Função principal para processar o dataset"""
    result = {}
    result['nome-arquivo'] = fname

    print(f"Carregando arquivo: {fname}")

    # Carregar dados
    data = pd.read_csv(fname, skipinitialspace=True, skip_blank_lines=True)

    print("=== DATASET ORIGINAL ===")
    dataset_info(data)

    # Remover valores inválidos
    data = remove_invalid_numbers(data)

    print("\n=== DATASET APÓS LIMPEZA ===")
    dataset_info(data)

    # Colunas categóricas para transformar (EXCLUDING the target column)
    mystr = 'workclass, education, marital-status, occupation, relationship, race, sex, native-country'
    process = [x.strip() for x in mystr.split(',')]

    # Verificar quais colunas existem no dataset
    existing_cols = []
    for col in process:
        if col in data.columns:
            existing_cols.append(col)
        else:
            print(f"Aviso: Coluna '{col}' não encontrada no dataset")

    # Se não encontrar as colunas pelos nomes, tentar pelos índices
    if len(existing_cols) == 0:
        print("Tentando identificar colunas por posição...")
        if len(data.columns) >= 14:  # Adult dataset tem 15 colunas
            categorical_indices = [1, 3, 5, 6, 7, 8, 9, 13]  # Posições das colunas categóricas (sem target)
            existing_cols = [data.columns[i] for i in categorical_indices if i < len(data.columns)]

    print(f"Colunas categóricas a serem processadas: {existing_cols}")

    # Transformar dados categóricos (sem incluir a coluna target)
    data = _transform_data(data, existing_cols)

    # Separar dados e classes ANTES da transformação da coluna target
    ultima = data.columns[-1]  # Última coluna (target/classe)
    target_values = list(data[ultima])  # Valores originais da coluna target

    # Convert target classes to binary (0/1) usando valores originais
    binary_classes = convert_target_to_binary(target_values)

    df = data.drop(columns=ultima)

    result['dados'] = df
    result['classes'] = binary_classes  # Now binary classes instead of encoded categorical
    result['colunas-categoricas'] = existing_cols
    result['total-linhas'] = len(df)
    result['total-colunas'] = len(df.columns)

    return result


def salvar_arquivos(fname, result):
    nome_base = fname.split('/')[-1].replace('.csv', '')

    arquivo_dados = f"{nome_base}--dados.csv"
    result['dados'].to_csv(arquivo_dados, index=False)
    print(f"Arquivo de dados salvo: {arquivo_dados}")

    arquivo_classes = f"{nome_base}--classes.csv"
    df_classes = pd.DataFrame({'classe': result['classes']})
    df_classes.to_csv(arquivo_classes, index=False)
    print(f"Arquivo de classes salvo: {arquivo_classes}")

    return arquivo_dados, arquivo_classes


if __name__ == '__main__':
    FNAME = '../datasets/adult.csv'

    print("=== PROCESSAMENTO DO DATASET ADULT ===")
    data = data_set(FNAME)

    print("\n=== RESUMO DO PROCESSAMENTO ===")
    for key, value in data.items():
        if key not in ['dados', 'classes']:
            print(f"{key}: {value}")

    fname = FNAME.split('/')[-1]
    print(f'\nfname --> {fname}')

    arquivo_dados, arquivo_classes = salvar_arquivos(FNAME, data)

    print(f"\n=== ARQUIVOS SALVOS ===")
    print(f"Dados: {arquivo_dados}")
    print(f"Classes: {arquivo_classes}")
    print(f"Total de linhas processadas: {data['total-linhas']}")
    print(f"Total de colunas de features: {data['total-colunas']}")