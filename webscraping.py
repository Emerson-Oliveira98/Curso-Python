from datetime import datetime #para marcar o dia e hora da extração
import requests #usadas para fazer a captura do conteúdo da página
import pandas as pd #para entregar os resultados em forma estruturada
from bs4 import BeautifulSoup #usadas para fazer a captura do conteúdo da página


texto_string = requests.get('https://globoesporte.globo.com').text #a propriedade text da biblioteca requests para capturar em formato de string
hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

bsp_texto = BeautifulSoup(texto_string, 'html.parser') #transformar essa string em formato html, para que possamos localizar as tags de nosso interesse
lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})#procuramos todas as tags div com o atributo que nos foi indicado

print('Quantidade de manchetes = ', len(lista_noticias))
lista_noticias[0].contents #  imprimimos o conteúdo da primeira notícia contents transforma cada início e final da div em um elemento da lista.

lista_noticias[0].contents[1].text.replace('"',"") #podemos ver que a manchete ocupa a posição 2 da lista de conteúdos, logo para guardar a manchete devemos fazer:

link = lista_noticias[0].find('a').get('href')#Para extração do link para notícia, como ele se encontra também na posição 1 da lista, vamos utilizar o método find('a') para localizá-lo e extrair

descricao = lista_noticias[0].contents[2].text
if not descricao:
    descricao = lista_noticias.find('div', attrs={'class ': 'bstn-related'})
    descricao = descricao.text if descricao else None # Somente acessará a propriedade text caso tenha encontrado ("find") descricao
descricao

metadados = lista_noticias[0].find('div',attrs={'class':'feed-post-metadata'}) #Para extração da seção e do tempo decorrido, vamos acessar primeiro o atributo 'feed-post-metadata' e guardar em uma variável

time_delta = metadados.find('span',attrs={'class': 'feed-post-datetime'})#localizar os atributos 'feed-post-datetime'
secao = metadados.find('span', attrs ={'class', 'feed-post-metadata-section'}) #localizar os atributos 'feed-post-metadata-section'

time_delta = time_delta.text if time_delta else None # garantir que somente acessaremos a propriedade text  caso tenha encontrando ("find")
secao = secao.text if secao else None # garantir que somente acessaremos a propriedade text  caso tenha encontrando ("find")

print('time_delta =', time_delta)
print('seção =',secao)

dados = [] #vamos criar uma lista vazia e a cada iteração apendar uma tupla com as informações extraídas
for noticia in lista_noticias:
    manchete = noticia.contents[1].text.replace('"',"")
    link = noticia.find('a').get('href')
    descricao = noticia.contents[2].text
    if not descricao:
        descricao = noticia.find('div', attrs={'class':'bstn-related'})
        descricao = descricao.text if descricao else None
    metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
    time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
    secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

    time_delta = time_delta.text if time_delta else None
    secao = secao.text if secao else None

    dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))

df = pd.DataFrame(dados, columns=['manchete', 'descricao', 'link', 'secao', 'hora_extracao', 'time_delta'])
df.head()
print(df)





