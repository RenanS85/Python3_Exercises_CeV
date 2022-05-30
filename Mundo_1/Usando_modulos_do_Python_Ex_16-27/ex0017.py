'''
EXERCÍCIO 017: Catetos e Hipotenusa
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

import math
print ('calculando a hipotenusa de um triangulo')
cateto1 = (float(input("digite um dos catetos do triangulo: ")))
cateto2 = (float(input("digite o outro cateto do triangulo: ")))
print('a hipotenusa é {}'.format(math.hypot(cateto1,cateto2)))