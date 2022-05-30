'''
EXERCÍCIO 064: Tratando Vários Valores v1.0
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
'''

c=0
s=0
n = int(input('Digite um numero: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite outro numero: '))
    if n == 999:
        print ('Foram digitados {} numeros e a soma deles é {}'.format(c,s))
        numeros = 0

