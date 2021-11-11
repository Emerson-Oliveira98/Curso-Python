lista = [10, 4, 1, 15, -3]
# A função built-in sorted() cria uma nova lista para ordenar e a retorna é guardada
# dentro da variável

lista_ordenada_1 = sorted(lista)

# o método sort(), da classe list, não cria uma nova lista, uma vez que faz a ordenação "inplace"
# (ou seja, dentro da própria lista passada como parâmetro).

lista_ordenada_2 = lista.sort()

print('lista = ', lista, '\n')
print('lista_ordenada_1 = ', lista_ordenada_1)
print('lista_ordnada_2 = ', lista_ordenada_2)
print('lista = ', lista)


# A essência dos algoritmos de ordenação consiste em comparar dois valores, verificar qual é menor e colocar na posição correta.

lista2 = [7, 4]
if lista2[0] > lista2[1]:
    aux = lista2[1]
    lista2[1] = lista2[0]
    lista2[0] = aux

print('lista2 = ', lista2)

# Em Python há "mágicas". Podemos fazer a troca usando a atribuição múltipla
lista3 = [5, -1,2,6]
if lista3[0] > lista3[1] and lista3[2] > lista[3]:
    lista3[0], lista3[1],lista3[2],lista3[3] = lista[3],lista3[1], lista3[0],lista[2]
print('lista3',lista3)










