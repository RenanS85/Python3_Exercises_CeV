'''
EXERCÍCIO 047: Contagem de Pares
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

for pares in range (1,50+1):
    if pares %2 == 0:
        print (pares, end=' ')

