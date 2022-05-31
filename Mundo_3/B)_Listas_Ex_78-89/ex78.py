'''
EXERCÍCIO 078: Maior e Menor Valores na Lista
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = []
for valores in range (0,5):
    lista.append(float(input('Digite um valor: ')))
maior = max(lista)
menor = min(lista)
posmaior = lista.index(maior)
posmenor = lista.index(menor)
print (f'o maior valor foi {maior} na posição {posmaior}')
print (f'o menor valor foi {menor} na posição {posmenor}')