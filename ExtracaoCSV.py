import pandas as pd

df_etanol = pd.read_csv('exportacao-etanol-hidratado-2012-2020-bep.csv', sep=';', encoding="ISO-8859-1")
df_etanol.drop(columns=['PRODUTO', 'MOVIMENTO COMERCIAL', 'UNIDADE'], inplace=True)
df_etanol.set_index(keys='ANO', drop=True, inplace=True)
for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ TOTAL'.split():
    df_etanol[mes]=df_etanol[mes].str.replace(',','.')
df_etanol = df_etanol.astype(float)
print(df_etanol.dtypes)
print(df_etanol)
df_etanol.head(2)

for ano in range(2012, 2021):
    ano_info = df_etanol.loc[ano]
    minimo = ano_info.min()
    maximo = ano_info.max()
    print(f"Ano = {ano}")
    print(f"Menor valor = {minimo:,.0f}".replace(',', '.'))
    print(f"Maior valor = {maximo:,.0f}".replace(',', '.'))
    print("--------------")

print("Media Mensal dos Rendimentos:")
for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split():
    media = df_etanol.loc[2012:2019, mes].mean()
    print(f"{mes} = {media:,.0f}".replace(',','.'))

ano_menor_arrecadacao = df_etanol.loc[2012:2019,'TOTAL'].idxmin()
ano_maior_arrecadacao = df_etanol.loc[2012:2019,'TOTAL'].idxmax()
print(f"Ano com menor arrecadação={ano_menor_arrecadacao}")
print(f"Ano com maior arrecadaçao={ano_maior_arrecadacao}")






