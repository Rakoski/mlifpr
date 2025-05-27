import numpy as np

letras = 'abcdefghijklmnopqrstuvwxyz@#*+'
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

lista = np.array(lista)

# # 13- capturar da tabela o elemento linha=2 e coluna=3, e imprimir na tela

tabela = np.matrix([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
                    ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
                    ['u', 'v', 'w', 'x', 'y', 'z', '@', '#', '*', '+']])

print("item: ", tabela.item(2, 3))

# # 14- transformar a tabela em um shape (10, 3), armazenar em tabela2.
# #       Imprimir cada linha da tabela2
# #       Comparar o resultado com a pergunta:

tabela2 = np.transpose(tabela)
for linha in tabela2:
    print("linha: ", linha)

# # 15- imprimir as colunas da tabela2

for coluna in tabela2.transpose():
    print("coluna: ", coluna)

# # 16- capturar da tabela, os elementos do meio, e colocar na variável: tabela3
# #       Imprimir a tabela3. Abaixo o que deve aparecer:
# #       ['h' 'i' 'j' 'k']
# #       ['n' 'o' 'p' 'q']
# #       ['t' 'u' 'v' 'w']
tabela3 = tabela[1:-1, 1:-1]
print('Tabela 3', tabela3)

# # 17 - essa lista abdcetc vamos refazer ela como linhas que contém 5 colunas e dessas 5 colunas pegar só os elementos do meio

tabela5 = lista.reshape(-1, 5)
print("lista: ", tabela5)
print(tabela5[1:-1, 1:-1])

# # 19- transformar a tabela 3 em uma lista, e colocar dentro da variável: lista3
# #       imprimir a lista3

print("shape 3: ", tabela3.shape)
print("shape 3: ", tabela5.shape)

lista3 = tabela3.tolist()
lista5 = tabela5.tolist()
print(lista3)
print(lista5)

# # 20- imprimir na tela, da lista3, os elementos de índice: 1, 4, 7 e 8
lista3 = tabela3.flatten()
lista5 = tabela5.flatten()

print(lista3)
print(lista5)

lista3 = [item for sublist in lista3 for item in sublist]
