'''
EXERCÍCIO 018: Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math
ang = (float(input('digite um angulo: ')))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print (f'O seno do angulo {ang} é {sen}, o cosseno do angulo é {cos} e a tangente do angulo é{tg}')