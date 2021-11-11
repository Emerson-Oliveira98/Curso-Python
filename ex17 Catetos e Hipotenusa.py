import math
from math import hypot

# Exercicio 17 quadrado da hipotenusa é igual a soma do quadrado dos catetos

co = float(input("Digite o Cateto Oposto: "))
ca = float(input("Digite o Cateto Adjacente: "))

hi = (co**2 + ca**2)**(1/2)  # forma matemática
funcaohi = hypot(co, ca) # Forma Python
print("A hipotenusa vai medir: {:.2f}".format(hi))
print("A hipotenusa via Python vai medir: {:.2f}".format(funcaohi))

