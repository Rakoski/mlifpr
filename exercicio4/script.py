# Escreva um programa que recebe uma lista de tuplas e retorna um dicionário que contém a contagem de cada tupla na lista.
def exerc4():
    ex4 = [(1, 2), (2, 3), (1, 2), (3, 4), (1, 2)]
    ret = {(1, 2): 3, (2, 3): 1, (3, 4): 1}

    return contaTUplas(ex4)

def contaTUplas(lista: list[tuple[type]]) -> dict[tuple[type], int]:
    conta = {}
    for valor in lista:
        if valor in conta:
            conta[valor] += 1
        else:
            conta[valor] = 1
    return conta

print(exerc4())
