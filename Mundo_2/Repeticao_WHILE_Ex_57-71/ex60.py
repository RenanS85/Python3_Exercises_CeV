'''
EXERCÍCIO 060: Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

from math import factorial
while True:
    try:
        n = int(input('Digite um número: '))
    except (ValueError,TypeError):
        continue
    else:
        break
c=n
while c > 1:
    print (f'{c} X ',end='')
    c -= 1
    if c == 1:
        print(f'{c} = {factorial(n)}', end='')
