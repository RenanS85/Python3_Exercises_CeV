'''
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

OBS: ex modificado para analisar se a cidade contém a palavra santo.
'''

cidade = input("digite o nome de sua cidade: ").lower()
cidade_split = cidade.split()
comeca = 'santo' in cidade_split[0]
contem = cidade_split.count('santo')
if comeca:
    print ('começa com santo')
else:
    comeca = False
    print ('nao começa com santo')

if not comeca and contem!= 0:
    print ('não começa, mas contém')

