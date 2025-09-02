# pip install scikit-learn
# pip install pandas

import numpy as np
from random import shuffle
from sklearn import metrics
from sklearn.impute import SimpleImputer
from sklearn.datasets import fetch_openml

from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def load_dataset():
    return fetch_openml(data_id=15, cache=False, as_frame=False)


def run_classification_experiment():
    """Executa um experimento de classificação completo"""

    # Carregando dados
    data = load_dataset()
    xdata = data.data
    ytarg = data.target

    # Verificando e tratando valores NaN
    print(f"Valores NaN encontrados: {np.isnan(xdata).sum()}")

    # Usando SimpleImputer para preencher valores NaN com a média
    imputer = SimpleImputer(strategy='mean')
    xdata = imputer.fit_transform(xdata)

    print(f"Valores NaN após tratamento: {np.isnan(xdata).sum()}")

    # Embaralhar os dados
    idx = list(range(len(ytarg)))
    shuffle(idx)
    xdata = xdata[idx]
    ytarg = ytarg[idx]

    part = int(len(ytarg) * 0.6)  # 60% para treino

    # Divisão treino/teste
    xtr = xdata[:part]
    ytr = ytarg[:part]
    xte = xdata[part:]
    yte = ytarg[part:]

    rng = np.random.RandomState(42)

    perceptron = Perceptron(max_iter=1000, random_state=rng)
    model_svc = SVC(probability=True, gamma='auto', random_state=rng)
    model_bayes = GaussianNB()
    model_tree = DecisionTreeClassifier(random_state=rng, max_depth=10)
    model_knn = KNeighborsClassifier(n_neighbors=7)

    clfs = {
        'perceptron': perceptron,
        'svm': model_svc,
        'bayes': model_bayes,
        'trees': model_tree,
        'knn': model_knn
    }

    results = {}
    ytrue = yte

    print('Treinando cada classificador e encontrando o score')
    for clf_name, classific in clfs.items():
        try:
            classific.fit(xtr, ytr)
            ypred = classific.predict(xte)

            # Calculando métricas
            matrconf = metrics.confusion_matrix(ytrue, ypred)
            acc = metrics.accuracy_score(ytrue, ypred)
            f1 = metrics.f1_score(ytrue, ypred, average='macro')

            results[clf_name] = {
                'accuracy': acc,
                'f1_score': f1,
                'confusion_matrix': matrconf
            }

            print(f'{clf_name} -- f1: {f1:.4f}, accuracy: {acc:.4f}')

        except Exception as e:
            print(f'Erro ao treinar {clf_name}: {e}')
            results[clf_name] = None

    return results


def run_multiple_experiments(num_experiments=20):
    """Executa múltiplos experimentos e calcula estatísticas"""

    all_results = {
        'perceptron': {'f1': [], 'accuracy': []},
        'svm': {'f1': [], 'accuracy': []},
        'bayes': {'f1': [], 'accuracy': []},
        'trees': {'f1': [], 'accuracy': []},
        'knn': {'f1': [], 'accuracy': []}
    }

    print(f"Executando {num_experiments} repetições do experimento...")
    print("=" * 50)

    for i in range(num_experiments):
        print(f"Repetição {i + 1}/{num_experiments}")

        results = run_classification_experiment()

        # Coletando resultados
        for clf_name, result in results.items():
            if result is not None:
                all_results[clf_name]['f1'].append(result['f1_score'])
                all_results[clf_name]['accuracy'].append(result['accuracy'])

        print("-" * 30)

    # Calculando estatísticas finais
    print("\n" + "=" * 50)
    print("RESULTADOS FINAIS (Média ± Desvio Padrão)")
    print("=" * 50)

    for clf_name, metrics_dict in all_results.items():
        if len(metrics_dict['f1']) > 0:
            f1_mean = np.mean(metrics_dict['f1'])
            f1_std = np.std(metrics_dict['f1'])
            acc_mean = np.mean(metrics_dict['accuracy'])
            acc_std = np.std(metrics_dict['accuracy'])

            print(f"{clf_name.upper()}:")
            print(f"  F1-Score:  {f1_mean:.4f} ± {f1_std:.4f}")
            print(f"  Accuracy:  {acc_mean:.4f} ± {acc_std:.4f}")
            print()


if __name__ == "__main__":
    # Executar experimento único
    # results = run_classification_experiment()

    # Executar múltiplos experimentos
    run_multiple_experiments(20)