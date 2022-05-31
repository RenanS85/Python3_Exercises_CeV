'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
três contagens através da função criada:
'''

def contator(i,f,p):
    for c in range(i,f,p):
        print(c,end= ' ')
    print(' ')


contator(1,10,2)
contator(20,1,-1)
contator(1,200,5)