
# Escreva um programa que recebe uma lista de objetos e retorna um dicionário que contém a contagem de cada objeto na lista.
def exerc5():
    ex5 = [1, 'apple', True, 'banana', 1, 'banana']
    ret = {1: 2, 'apple': 1, True: 1, 'banana': 2}

    return contaDicks(ex5)

def contaDicks(lista: list) -> dict:
    conta = {}
    for valor in lista:
        if type(valor) == bool:
            if valor == True:
                if True in conta:
                    conta[True] += 1
                else:
                    conta[True] = 1
            else:
                if False in conta:
                    conta[False] += 1
                else:
                    conta[False] = 1
        else:
            if valor in conta:
                conta[valor] += 1
            else:
                conta[valor] = 1
    return conta
print(exerc5())