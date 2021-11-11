import pandas as pd
series1 = pd.Series(data=5) # Cria uma Series com o valor a
print(series1)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
series2 = pd.Series(lista_nomes)
print(series2)

dados ={'nome1':'Howard',
        'nome2':'Ian',
        'nome3':'Peter',
        'nome4':'Jonah',
        'nome4':'Kellie',}
series3 = pd.Series(dados)
print(series3)

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
series4 = pd.Series(cpfs)
print(series4)





