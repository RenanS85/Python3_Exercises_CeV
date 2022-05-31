'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que
analisar todos os valores e dizer qual deles é o maior.
'''

def maior (*n):
    l = []
    for num in n:
        l.append(num)
    org = sorted(l,reverse=True)
    return f'{org[0]} é o maior número'
