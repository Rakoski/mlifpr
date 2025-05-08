
# Escreva um programa que recebe uma lista de valores booleanos e retorna um dicionário que contém a contagem de cada valor na lista.
def exerc3():
    ex3 = [True, False, True, False, True]
    alooo = [1, 2, 5, 5, 2, 10]
    ret = {'True': 3, 'False': 2}
    return [contagem(ex3), contagem(alooo)]

def contagem(valores: list) -> dict[type, int]:
    conta = {}
    for valor in valores:
        if valor in conta:
            conta[valor] += 1
        else:
            conta[valor] = 1
    return conta

print(exerc3())



