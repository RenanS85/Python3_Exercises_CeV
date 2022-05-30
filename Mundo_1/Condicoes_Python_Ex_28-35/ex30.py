'''
EXERCÍCIO 030: Par ou Ímpar?
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

OBS: modificado para o programa gerar um número aleatório, simulando uma escolha do usuário.
'''

for numero in range (10001):
    numero

import random
n = random.randrange(numero)
print ('o numero sorteado é {}'.format(n))

if n%2 == 0:
    print ('o numero {} é par'.format(n))
else:
    print ('o numero {} é impar'.format(n))