'''
EXERCÍCIO 079: Valores Únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
'''

lista = []
n = 0
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        print ('Numero adiconado com sucesso')
    elif n in lista:
        print('Esse numero ja exist e não sera adcionado...')
    quer = input('Quer continuar[s/N]: ').strip().upper()
    while quer not in 'SsNn':
        quer = input('Quer continuar[s/N]: ').strip().upper()
    if quer in 'Nn':
        break
lista.sort()
print (lista)

