'''
EXERCÍCIO 052: Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

n = (int(input('digite um numero: ')))

tot = 0
for c in range (1,n+1):
    if n%c==0:
        print ('\033[33m', end=' ')
        tot += 1
    else:
        print ('\033[31m', end= ' ')
    print ('{}'.format(c), end=' ')

print (' ')

print ('\nO numero {} foi dividido {} vezes'.format(n,tot))
if tot == 2:
    print ('ele é primo')
else:
    print ('ele não é primo')









