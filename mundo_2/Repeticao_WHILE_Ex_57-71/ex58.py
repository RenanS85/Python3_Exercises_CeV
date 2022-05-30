'''
EXERCÍCIO 058: Jogo da Adivinhação v2.0
Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''

import random
import time
n = random.randint(0,5)
print ('-=-'*20)
print ('vou pensar num numero de 0 a 5, tente adivinhar...')
print ('-=-'*20)
print ('Estou pensando')
time.sleep(3)
n2 = int(input('Qual é o numero certo?'))
tot_tenta = 0
while n!=n2:
    n2 = int(input('tente novamente: '))
    tot_tenta += 1
print (f'top, vc acertou, mas precisou de {tot_tenta+1} tentativas.')