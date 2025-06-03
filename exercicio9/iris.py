import pandas as pd

df = pd.read_csv('./iris.csv')

with open("./iris.csv") as oii:
    tmp = oii.read()
    splitado = tmp.split(",")
    for a in splitado:
        if "Iris" in a and "4" not in a and "5" not in a and "6" not in a and "7" not in a:
            print(a)
    oii.close()

