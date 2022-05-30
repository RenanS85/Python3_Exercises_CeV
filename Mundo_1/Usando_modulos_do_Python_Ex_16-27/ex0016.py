'''
EXERCÍCIO 016: Quebrando um Número
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''

import math
print ('lendo um numero real em sua porção inteira')
n = float(input('digite um numero com casas decimais: '))

'''MANEIRA 1'''
print('sua porção inteira é {}'.format(math.floor(n)))

'''MANEIRA 2'''
print('sua porção inteira é {}'.format(math.trunc(n)))

