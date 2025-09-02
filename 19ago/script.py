# pip install scikit-learn
# pip install pandas

from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from random import shuffle


def capturar_dados():
    """
    Carrega e preprocessa o dataset Wisconsin Breast Cancer do arquivo CSV
    """
    # Carregar dados do arquivo CSV, tratando '?' como NaN
    df = pd.read_csv('breast-cancer-wisconsin.csv', na_values='?')

    print(f"Dataset carregado: {len(df)} amostras")
    print(f"Colunas: {list(df.columns)}")

    # Verificar se há valores faltantes
    missing_values = df.isnull().sum()
    if missing_values.any():
        print(f"Valores faltantes encontrados:")
        print(missing_values[missing_values > 0])

    print(f"Distribuição das classes: {df['classe'].value_counts().to_dict()}")

    # Tratar valores faltantes - substituir pela mediana de cada coluna
    # (exceto uuid e classe)
    features_cols = df.drop(['uuid', 'classe'], axis=1).columns
    for col in features_cols:
        if df[col].isnull().any():
            median_value = df[col].median()
            df[col].fillna(median_value, inplace=True)
            print(f"Valores faltantes na coluna '{col}' substituídos pela mediana: {median_value}")

    # Separar features (X) e target (y)
    X = df.drop(['uuid', 'classe'], axis=1).values
    y = df['classe'].values

    # Converter classes: 2 (benigno) -> 0, 4 (maligno) -> 1
    y = np.where(y == 2, 0, 1)

    return {'dados': X, 'classes': y}


def avaliar_classificador(clf, xtreino, ytreino, xteste, yteste):
    """
    Treina e avalia um classificador
    """
    clf.fit(xtreino, ytreino)
    yhat = clf.predict(xteste)
    score = metrics.accuracy_score(yteste, yhat)
    return score


def run_experiment():
    """
    Executa um experimento comparando SVC e Perceptron
    """
    data = capturar_dados()
    xdata = data['dados']
    ytarg = data['classes']

    xdata = np.array(xdata)
    ytarg = np.array(ytarg)

    # Embaralhar os dados
    nums = list(range(len(ytarg)))
    shuffle(nums)

    xdata = xdata[nums]
    ytarg = ytarg[nums]

    size = len(ytarg)
    particao = int(size * 0.6)  # treino -> 60%, teste -> 40%

    xtreino = xdata[:particao]
    ytreino = ytarg[:particao]

    xteste = xdata[particao:]
    yteste = ytarg[particao:]

    # Inicializar classificadores
    perceptron = Perceptron(max_iter=1000, random_state=42)
    svc = SVC(kernel='linear', random_state=42)

    # Avaliar classificadores
    perceptron_score = avaliar_classificador(perceptron, xtreino, ytreino, xteste, yteste)
    svc_score = avaliar_classificador(svc, xtreino, ytreino, xteste, yteste)

    return perceptron_score, svc_score


def main():
    """
    Executa 20 experimentos e calcula médias
    """
    perceptron_scores = []
    svc_scores = []

    print("Executando 20 experimentos...")
    print("-" * 50)

    for idx in range(20):
        print(f'Executando experimento {idx + 1}/20')
        perceptron_score, svc_score = run_experiment()

        perceptron_scores.append(perceptron_score)
        svc_scores.append(svc_score)

        print(f'  Perceptron: {perceptron_score:.4f} | SVC: {svc_score:.4f}')

    print("-" * 50)
    print("RESULTADOS FINAIS:")
    print("-" * 50)

    # Calcular médias
    avg_perceptron = np.mean(perceptron_scores)
    avg_svc = np.mean(svc_scores)

    # Calcular desvios padrão
    std_perceptron = np.std(perceptron_scores)
    std_svc = np.std(svc_scores)

    print(f"Perceptron:")
    print(f"  Acurácia Média: {avg_perceptron:.4f} ± {std_perceptron:.4f}")
    print(f"  Scores individuais: {perceptron_scores}")

    print(f"\nSVC:")
    print(f"  Acurácia Média: {avg_svc:.4f} ± {std_svc:.4f}")
    print(f"  Scores individuais: {svc_scores}")

    print(f"\nComparação:")
    if avg_svc > avg_perceptron:
        print(f"SVC é melhor por {avg_svc - avg_perceptron:.4f} pontos de acurácia")
    elif avg_perceptron > avg_svc:
        print(f"Perceptron é melhor por {avg_perceptron - avg_svc:.4f} pontos de acurácia")
    else:
        print("Ambos os algoritmos têm desempenho similar")


if __name__ == "__main__":
    main()