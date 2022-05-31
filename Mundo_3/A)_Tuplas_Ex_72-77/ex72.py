'''
EXERCÍCIO 072: Número por Extenso
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

from num2words import num2words

lista = []
for n in range (0,21):
    num_ptbr = num2words(n, lang='pt-br')
    lista.append(num_ptbr)
tupla = tuple(lista)

n = int(input('digite um numero entre 0 e 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('digite um numero entre 0 e 20: '))
    else:
        print (f'voce digitou o numero {tupla[n]}')
        break


