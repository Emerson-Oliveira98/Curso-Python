import pandas as pd

### dataframe = pd.DataFrame()
venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
     'produtos': ['feijao', 'arroz'],
        'qtde': [50, 70],
    }
vendas_df2 = pd.DataFrame(venda)
##vendas_df = pd.DataFrame(venda)
### visualização   print e display

print(vendas_df2)



#### importar de uma base de dados
## se tiver em outra pasta voce coloca "C://###//##"
vendas_df = pd.read_excel("Vendas.xlsx")
#print(vendas_df)  #mostra tudo


### head = mostra os 5 primeiro  shape = mostra conta quantas linhas tem   describe = resumo (colunas numericas. quantidade de linhas e da media dos preços faturamento e desvio padrão)

print(vendas_df.head(10))
print(vendas_df.shape)
print(vendas_df.describe())



#################################
#### editar a tabela  pegar informação so de uma coluna
## Para pegar mais de uma coluna usa dois conceites [['coluna', 'coluna']]
produtos = vendas_df['Produto']
print(produtos)



#### pegar linha  .loc  se for pegar mais linha [1:?]
print(vendas_df.loc[1])



## pegar linhas que correspondem a uma condição  vendas_df['ID Loja'] =='Norte Shopping'

print(vendas_df.loc[vendas_df['ID Loja'] =='Norte Shopping'])

## para atrinuir resultado na variavel   
## vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] =='Norte Shopping']


## pegas varias linhas  e colunas usando o loc
## padrao  linhas, colunas
## vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] =='Norte Shopping', ["ID Loja", "Produto", "Quantidade"]]


### pegar 1 valor especifico
### print(vendas_df.loc[linha, coluna])


### adicionar coluna nova
# apartir de uma coluna que existe
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
print(vendas_df)

# criar uma coluna com valor padrão
#vendas_df['Imposto'] = 0
#vendas_df.loc[linha, coluna] = 0
## : usar para tudo
vendas_df.loc[:, "Impostos"] = 0


### adicionar linhas

# atribuir valor da tabela excel em uma variavel
vendas_des_df = pd.read_excel("Vendas-Dez.xlsx")

# adiciona variavel tabela excel em outra tabela
vendas_df = vendas_df.append(vendas_des_df)

####### excluir linhas e colunas
# axis=0  é linhas             asxis=1  é coluna
##vendas_df = vendas_df.drop("Imposto", axis=1) #metodo para escluir



##########Valores vazios

## deletar linhas e colunas completamnete vazis
##vendas_df = vendas_df.dropna(how='all') excluir as linhas aonde esta tudo vazio
#vendas_df = vendas_df.dropna(how='all', axis=1) excluir as colunas aonde esta tudo vazio

## deletar linhas que possuem pelo menos 1 valor vazio
##vendas_df = vendas_df.dropna()  excluir linhas que tem pelos menos um campo vazio

## preencher valores vazios
#preencher com a media da coluna
#vendas_df['Comissão'] = vendas_df['Comissão'].fillna(0) #preenche com 0 todos os valores de comissão que estão vazios

#vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) # preenche todos os campos em vazio com a media da coluna comissão


## preencher com o ultimo valor

##vendas_df - vendas_df.ffill() preencher todos os valores em branco e pega o valor de cima e arrasta para baixo colando


### calcular  Indicadores

#transacoes_loja = vendas_df['ID Loja'].value_counts() # conta quantas linhas tem cada loja

# sum = somar    mean = media
## group by
#faturamento_produto = vendas_df.groupby('Produto').sum() #agrupa as linhas com produto igual e soma os demais valores com da linha produto igual
#faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum() # mesma coisa do de cima so que mostra as duas colunas pedidas



# mesclar  = merge
#gerentes_df = pd.read_excel("Gerentes.xlsx") #guardar tabela excel em uma variavel

#vendas_df = vendas_df.merge(gerentes_df) # mescla todas as informações de uma tabela em outra e identifica um padrão para usar com primaria key





