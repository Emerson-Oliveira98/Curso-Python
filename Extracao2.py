import pandas as pd
dadosjson = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
print(dadosjson)
dados2 = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv",sep=',').head()
print(dados2)



