'''
EXERCÍCIO 063: Sequência de Fibonacci v1.0
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
'''

n = int(input('Digite um numero: '))
t1 = 0
t2 = 1
print (' {} , {} ,'.format(t1,t2),end='')
c=3
while c <= n:
    t3 = t1 + t2
    print (' {} ,'.format(t3), end='')
    t1=t2
    t2=t3
    c+=1
print (' fim')

