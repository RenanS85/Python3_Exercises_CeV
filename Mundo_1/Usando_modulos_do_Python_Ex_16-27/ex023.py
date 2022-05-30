'''
EXERCÍCIO 023: Separando Dígitos de um Número
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
'''

num = input('digite um número entre 0 e 9999: ')
m = 'milhar'
c = 'centena'
d = 'dezena'
u = 'unidade'

reverso=[]
for n in reversed(num):
    reverso.append(n)

cont = 0
for n in reverso:
    if cont == 0:
        print (f'{u}: {reverso[cont]}')
    if cont == 1:
        print(f'{d}: {reverso[cont]}')
    if cont == 2:
        print(f'{c}: {reverso[cont]}')
    if cont == 3:
        print(f'{m}: {reverso[cont]}')
    cont+=1