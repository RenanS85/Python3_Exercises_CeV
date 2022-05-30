'''
EXERCÍCIO 020: Sorteando uma Ordem na Lista
O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random
from time import sleep
c=1
lista = []
for aluno in range (4):
    a= (input(f'aluno {c}: ')).strip().title()
    lista.append(a)
    c+=1

random.shuffle(lista)
print('SORTEIO: ')
c=1
for aluno in lista:
    sleep(0.5)
    print (f'{c}º da ordem: {aluno}')
    c+=1