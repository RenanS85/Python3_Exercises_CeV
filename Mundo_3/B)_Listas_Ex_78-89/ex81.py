'''
Extraindo Dados de uma Lista
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    quer = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while quer not in 'SsNn':
        quer = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if quer in 'Nn':
        break
print (f'Foram digitados {len(lista)} números')
if 5 in lista:
    print (f'O valor 5 esta na lista na posição {lista.index(5)}')
else:
    print ('não teve numero 5')
lista.sort(reverse=True)
print (f'lsita em organização decrescente: {lista}')


