'''
EXERCÍCIO 028: Jogo da Adivinhação v1.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random
import time
n = random.randint(0,5)
print ('-=-'*20)
print ('vou pensar num numero de 0 a 5, tente adivinhar...')
print ('-=-'*20)
print ('Estou pensando')

for c in range (3):
    time.sleep(0.5)
    print('.',end='')

time.sleep(0.5)
n2 = int(input('\nQual é o numero certo?: '))
if n2 == n:
    print ('Voce acertou')
else:
    print('voce errou o numero é {}'.format(n))