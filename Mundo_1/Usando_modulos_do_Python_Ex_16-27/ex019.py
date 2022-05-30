'''
EXERCÍCIO 019: Sorteando um Item na Lista
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

import random
c=1
lista = []
for aluno in range (4):
    a= (input(f'aluno {c}: ')).strip().title()
    lista.append(a)
    c+=1

sort = random.choice(lista)
print (f'O aluno sorteado foi o/a {sort}!!!')


