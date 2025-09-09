import numpy as np
from random import shuffle
from sklearn import metrics
import pandas as pd
from sklearn.datasets import fetch_openml

from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

class Dataset:
    def __init__(self, data, target):
        self.data = data
        self.target = target


def load_dataset():
    FNAME = 'adult.csv'

    df = pd.read_csv(FNAME, skipinitialspace=True, skip_blank_lines=True)

    cols = list(df.columns)
    target_col = cols[-1]

    y = df[target_col]
    X = df.drop(columns=[target_col])

    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()

    for col in categorical_cols:
        X[col] = X[col].fillna('Unknown')
        unique_vals, encoded_vals, counts = np.unique(X[col], return_inverse=True, return_counts=True)
        X[col] = encoded_vals
        print(f"tiveream {col}: {len(unique_vals)} categorias")

    numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()

    for col in numerical_cols:
        X[col] = X[col].fillna(X[col].median())
        min_val = X[col].min()
        max_val = X[col].max()
        if max_val != min_val:
            X[col] = (X[col] - min_val) / (max_val - min_val)
        print(f"colunas: {col}: range ta entre [{min_val:.2f}, {max_val:.2f}] -> [0, 1]")

    y_unique, y_encoded, y_counts = np.unique(y, return_inverse=True, return_counts=True)
    print(f"classes: {y_unique}, contas: {y_counts}")

    data = Dataset(X.values, y_encoded)
    return data


data = load_dataset()
alldata = data.data
alltarg = data.target


results = {
            'perceptron':   [],
            'svm':          [],
            'bayes':        [],
            'trees':        [],
            'knn':          []
}

rng = np.random.RandomState()

def get_cv_value(xdata, ytarg):

    part = int(len(ytarg)*0.8) # assumindo 80%
    parcial_result = {
                'perceptron':   [],
                'svm':          [],
                'bayes':        [],
                'trees':        [],
                'knn':          []
    }

    for crossv in range(5):

        # xtr --> x_treino  ;  xte --> x_teste
        xtr = xdata[ :part ]
        ytr = ytarg[ :part ]
        xte = xdata[ part: ]
        yte = ytarg[ part: ]


        perceptron = Perceptron(max_iter=100,random_state=rng)
        model_svc = SVC(probability=True, gamma='auto',random_state=rng)
        model_bayes = GaussianNB()
        model_tree = DecisionTreeClassifier(random_state=rng, max_depth=10)
        model_knn = KNeighborsClassifier(n_neighbors=7)

        clfs = {
                    'perceptron':   perceptron,
                    'svm':          model_svc,
                    'bayes':        model_bayes,
                    'trees':        model_tree,
                    'knn':          model_knn
                }

        ytrue = yte
        for clf_name, classific in clfs.items():
            classific.fit(xtr, ytr)
            ypred = classific.predict(xte)
            f1 = metrics.f1_score(ytrue, ypred, average='macro')
            print(clf_name, '-- f1:', f1)
            parcial_result[clf_name].append( f1 )


        ytarg = list(ytarg[ part: ]) + list(ytarg[ :part ])
        xdata = list(xdata[ part: ]) + list(xdata[ :part ])

        print('####\n####')

    for clf_name, result in parcial_result.items():
        value = sum(result)/len(result)
        print(clf_name, '-->', value)
        parcial_result[clf_name] = value

    return parcial_result


def principal():
    for exec_id in range(3):
        idx = list(range(len(alltarg)))
        shuffle(idx)
        xdata = alldata[ idx ]
        ytarg = alltarg[ idx ]
        ret = get_cv_value(xdata, ytarg)
        print(ret)


principal()


