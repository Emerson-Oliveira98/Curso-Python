import pandas
import matplotlib
import inline
import matplotlib.pyplot as plt

file = open('relatorio_jogos.txt','r')
print('file = ',file, '\n')
info_relatorio = file.readlines()
file.close()

print("linha = 1 ", info_relatorio[0])

# Extrair somente a parta 'dd/mm' da linha
datas = [linha[1:6] for linha in info_relatorio]
print(sorted(datas))

# Então, para remover as duplicações, vamos utilizar o construtor set().
datas_count = [(data, datas.count(data)) for data in set(datas)]
print(datas_count)

# vamos transformar essa lista em um dicionário usando o construtor dict()

datas_count = dict(datas_count)
print(datas_count)

eixo_x = datas_count.keys()
eixo_y = datas_count.values()


plt.xlabel('Dia do Mês')
plt.ylabel('Quantidade de Jogos')
plt.xticks(rotation=45)

plt.show()




