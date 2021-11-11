import pandas
import matplotlib
import numpy
from matplotlib import pyplot as plt

x = range(10)
x = numpy.array(x)
img, ab = plt.subplots(1,2, figsize=(10,10))
print("Tipo de ab = ", type(ab))
print("Conteudo de ab[0]=", ab[0])
print("Conteudo de ab[1]=", ab[1])

ab[0].plot(x,x, label='eq_1')
ab[0].plot(x,x**2, label='eq_2')
ab[0].plot(x,x**3, label='eq_3')
ab[0].set_xlabel('Eixo x')
ab[0].set_ylabel('Eixo y')
ab[0].set_title("Gráfico 1")
ab[0].legend()

ab[1].plot(x,x,'r--',label='eq_1')
ab[1].plot(x**2,x,'b--',label='eq_2')
ab[1].plot(x**3, x,'g--', label='eq_3')
ab[1].set_xlabel('Novo Eixo x')
ab[1].set_ylabel('Novo Eixo y')
ab[1].set_title("Gráfico 2")
ab[1].legend()
plt.show()

