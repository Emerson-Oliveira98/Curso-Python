frase = 'Curso em Video Python'
#        ----- -- -----   ------
#        01234 56 7891011 121314151617
# Fatiamento
print(frase[9]) # Pegar uma letra pelo indice
print(frase[9:13]) # Pegar do 9 até o 12 o 13 é excluido
print(frase[9:21]) # Pegar do 9 até o 20 o 21 é excluido
print(frase[9:21:2]) # Pegar do 9 até o 12 o 20 pulando de 2 en 21 é excluido
print(frase[:5]) # Pegar do começo até 5 e o 5 é excluido
print(frase[15:]) # Pegar do 15 até o final
print(frase[9::3]) # Pegar do 9 até o fim de 3 em 3

# Análise
print(len(frase)) # Contar o tamanho de frase
print(frase.count('o')) # Contar quantas vezes aparece 'o'
print(frase.count('o', 0, 13)) # Contar com fatiamento
print(frase.upper().count('O'))
print(frase.find('deo')) # Mostrar o inicio de quando deo é encontrada
print(frase.find('Android'))# Quando não exite find retorna -1
print('Curso' in frase) # Exite a palavra Curso em frase ? True ou False

# Transformação Via de regra uma string é imutável mas consigo mudá-la através dos métodos
print(frase.replace('Python','Android')) #Trocar uma palavra por outra
# para mudar a string frase preciso atribuir a mudança
# frase = print(frase.replace('Python','Android'))
print(frase.upper())# Transforma em maiúsculo
print(frase.lower()) #Transforma em minúsculo
print(frase.capitalize())# Tudo em minúsculo somente a primeira em maiúscula
print(frase.title())# Muda para maiúsculo a primeira letra de cada palavra
frase2= "   Aprenda Python   "
print(frase2.strip())#Remove os espaços inuteis no início e no final da string
print(frase2.rstrip())#Remove somente os espaços da direita
print(frase2.lstrip())#Remove somente os espaços da esquerda

# Divisão
print(frase.split()) # Divisão da String em cada espaço e colocar em uma lista

# Junção
print('-'.join(frase)) # Junta todos os caracteres com um '-' entre eles


dividido=(frase.split())
print(dividido[2])
print(dividido[2][3])
