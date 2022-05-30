'''
EXERCÍCIO 033: Maior e Menor Valores
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

c=1
lista = []
for n in range (3):
    n = float(input(f'DIGITE O {c}º NÙMERO: '))
    lista.append(n)
    c+=1

lista2 =sorted(lista)

print ('{} > {} > {}'.format(lista2[2],lista2[1],lista2[0]))

