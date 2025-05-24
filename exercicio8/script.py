import numpy as np

letras = 'abcdefg'
lista = list(letras)

# 10 primeiros elementos
print(lista [ : 10 ])

# 10 últimos elementos
print(lista [ -10: ])

meio = len(lista) / 2
meio = int(meio)
print(lista[meio - 5 : meio + 5])

tab = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tab = np.array(tab)
print(tab)
print('ndim --> ', tab.ndim)

print('mostrando indice: ', tab[1, 1])

print('última linha: ', tab[-1])

print('rafael: ', tab[::-1])

print('coluna meio: ', tab [ :, 1])

diagonal = []

for i in range(len(tab)):
    diagonal.append(tab[i, i])

print("diagonal: ", diagonal)

#transpose -> coluna vira linha e linha vira coluna

tabela = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tabela_t = np.transpose(tabela)

print("transpose: ", tabela_t)

lista2 = [1, 2, 3]

lista2_novo_formato = np.reshape(lista2, 3)

print("reshape: ", lista2_novo_formato)