import math #podemos importar todas os métodos
from math import sqrt # ou podemos importar somente a funcionalidade
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é {}".format(num,math.ceil(raiz))) #arredondar para baixo e math.flor(raiz)

import random
num= random.random() # gerar numero aleatório
num2=random.randint(1,10) # gerar um numero inteiro aleatório de 1 a 10
print(num)
print(num2)

#https://docs.python.org/3.6/library/index.html endereço das bibliotecas

#import emoji #Imprimir emojis
#print (emoji.emojize( "Python is :thumbs_up:", use_aliases=True ))







