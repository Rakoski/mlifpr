import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50])
print("Before shuffle (1D):", arr_1d)
np.random.shuffle(arr_1d)
print("After shuffle (1D):", arr_1d)

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)
