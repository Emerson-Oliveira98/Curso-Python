import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# Vamos pegar cotação do Indice e de Petrobras

# Indice
df = web.DataReader(f'^BVSP', data_source ='yahoo', start=f'02-20-2020', end='01-20-2021')

print(df)