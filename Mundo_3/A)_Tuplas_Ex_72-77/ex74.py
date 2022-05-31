'''
EXERCÍCIO 074: Maior e Menor Valores em Tupla
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
'''

from random import randint
list = []
for n in range (0,5):
    n = randint(0,200)
    list.append(n)

tupla = tuple(list)
print(tupla)

print (f'o maior é {max(tupla)} e o menor é {min(tupla)}')



