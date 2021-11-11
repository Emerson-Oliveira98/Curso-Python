def BuscaSeq(lista, item):
    pos = 0
    x= False
    while pos < len(lista) and not x:
        if lista[pos] == item:
            x = True
        else:
            pos = pos + 1
    return x
lista = [5, 6, 7, 8, 12, 1, 5, 7]
print(BuscaSeq(lista, 8))
print(BuscaSeq(lista, 13))

