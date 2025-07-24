import numpy as np
import pandas as pd

fname = 'aaa.csv'
data = pd.read_csv(fname, header = None)
mascara = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mascara[7] = 1
mascara[15] = 1
mascara[19] = 1

mascara = np.array(mascara, dtype=bool)
df = data[mascara]
print(df)