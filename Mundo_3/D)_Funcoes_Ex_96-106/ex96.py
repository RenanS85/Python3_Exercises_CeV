'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
'''

def area(l1,l2):
    '''
    Calculadora de área (m²)
    :param l1: lado número 1
    :param l2: lado número 2
    :return: área (m²)
    '''
    a = l1 * l2
    return f'a área entre {l1}m e {l2}m é {a}m²'

l1 = float(input('Lado numero 1: '))
l2 = float(input('Lado numero 2: '))
a = area(l1,l2)
print(a)
