import inline
import matplotlib

from Matplotlib import datas_count
%matplotlib inline
import matplotlib.pyplot as plt

eixo_x = datas_count.keys()
eixo_y = datas_count.values()

plt.figure(figsize(15,5))
plt.xlabel('Dia do Mês')
plt.ylabel('Quantidade de Jogos')
plt.xticks(rotation=45)

plt.show()
