
def conta(lista):
    result = [0, 0, 0]
    for id in lista:
        idx = id-1
        result[idx] = result[idx]+1
        print(result[idx]+1)
    print('resultado ==>', result)

def conta_dict(lista):
    result = {'1': 0, '2': 0, '3': 0}

conta([1, 2, 3, 2, 1, 2, 3, 1, 2])