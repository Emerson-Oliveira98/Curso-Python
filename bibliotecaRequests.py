import requests
info = requests.get('https://api.github.com/events')
info.headers

print(info.headers ['date']) # Data de extração
print(info.headers['server']) # Servidor de origem
print(info.headers['status']) # Status HTTP da extração, 200 é ok
print(info.encoding)  # Encoding do texto
print(info.headers['last-modified']) # Data da última modificação da informação

texto_str = info.text
print(type(texto_str))
texto_teste = texto_str[:100]  #exibe somente os 100 primeiros caracteres
print(texto_teste)

texto_json = info.json()
print(type(texto_json))
texto_teste2 = texto_json[0]
print(texto_teste2)





