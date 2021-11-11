from random import shuffle
#Exercicio 20 faça um programa que leia o nome dos 04 alunos e mostre a ordem sorteada

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))
lista = [a1, a2, a3, a4]
# embaralhar a lista
shuffle(lista)
print("O Aluno sorteado foi", lista)