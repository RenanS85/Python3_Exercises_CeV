'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear
5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteia():
    l = []
    for sort in range (5):
        sort = randint(1,500)
        l.append(sort)
    return l

def somaPar(list):
    s=0
    for n in list:
        if n%2 == 0:
            s+=n
    return f'A soma dos pares é {s}'


lista = []
s = sorteia()
print(s)
for n in s:
    lista.append(n)
soma_par = somaPar(lista)
print(soma_par)

