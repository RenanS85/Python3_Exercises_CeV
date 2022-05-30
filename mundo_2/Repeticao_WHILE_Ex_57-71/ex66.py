'''
EXERCÍCIO 066: Vários Números com Flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

c=s=0
while True:
    n = float(input('Digite um numero: '))
    if n != 999:
        s+=n
        c+=1
    elif n == 999:
        break
print (f'vc digitou {c} numeros e a somatoria deles é {s}')
