import copy
lista_a = ["Lira", "Alon", "Julia", "Jessica"]

lista_b = lista_a
lista_b.append("Feijao")
print(lista_a)
print(lista_b)

texto_a = "Lira"
texto_b = texto_a
texto_b = texto_b.replace("L", "B")
print(texto_a)
# 2 formas  receber os elementos do lista
#lista_c = lista_a[:]   ou   lista_c = lista_a.copy()
lista_c = lista_a[:]
lista_c.append("Arroz")
print(lista_a)
print(lista_c)


### para listas de listas, temos que pensar diferente
produtos = [
    ["Ipad", 5000],
    ["Iphone", 4500]
]

produtos2 = produtos[:]
produtos[0][1] = 6000
print(produtos)
print(produtos2)


### solução é um deepcopy

produtos3 = copy.deepcopy(produtos)
produtos3[0][1] = 1000
print(produtos)
print(produtos3)