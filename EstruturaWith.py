#Estrutura With

# sem with

arquivo = open("meu arquivo.txt", "w")
arquivo.write("Eita Lrinha, manda video novo pasra gente ai")
arquivo.close()


## Com o with ele abre o arquivo e fecha depois
with open("meu_arquivo.txt", 'w') as arquivo:
    arquivo.write("Eai Lira, tranquilao?")

with open("meu_arquivo.txt", 'r') as arquivo:
    print(arquivo.read())
 