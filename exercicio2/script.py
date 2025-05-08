def conta(lista):
    c1, c2, c3 = 0, 0, 0

    for vlr in lista:
        if vlr == 1:
            c1 += 1
        elif vlr == 2:
            c2 += 1
        elif vlr == 3:
            c3 += 1
        else:
            print('valor nao reconhecido:', vlr)

    print('c1 ->', c1)
    print('c2 ->', c2)
    print('c3 ->', c3)


def conta_v2(lista):
    lc = [0]*3

    for vlr in lista:
        idx = vlr - 1
        lc[idx] = lc[idx] + 1
        #print('valor nao reconhecido:', vlr)

    for idx, cnt in enumerate(lc):
        print(f'c{idx+1} -> {cnt}')


def conta_v3(lista):
    dc = {}

    for vlr in lista:
        if vlr in dc:
            dc[vlr] = dc[vlr] + 1
        else:
            dc[vlr] = 1

    for key, ctn in dc.items():
        print(f'{key} -> {ctn}')



conta([1, 2, 3, 2, 1, 2, 3, 1, 2])
print('-----')
conta_v2([1, 2, 3, 2, 1, 2, 3, 1, 2])
print('-----')
conta_v3([1, 2, 3, 2, '1', 2, 3, 1, 2, 4, 4, 'mar', 'banana', 4, 'mar'])