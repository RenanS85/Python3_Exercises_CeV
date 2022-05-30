'''
EXERCÍCIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''

frase = (str(input('Digite uma palavra: '))).strip().upper()
frase_join = ' '.join(frase)
frase_split = frase_join.split()

frase_reversa = []

for _letra in frase_split[::-1]:
    frase_reversa.append(_letra)

if frase_split == frase_reversa:
    print ('è um palindromo')
else:
    print ('Não é um Palíndromo')












