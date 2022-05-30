'''
EXERCÍCIO 005: Antecessor e Sucessor
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
SE O NÚMERO NÃO FOR INTEIRO O PROGRAMA DEVE ENCERRAR COM ValueError.
'''
import sys
print ('DESAFIO 5:',end='')
print ('escolher um número inteiro, e o programa ler seu antecessor e sucessor')

try:
    n = int(input ('escolha um número: '))
    print ('seu número é {}, seu antecessor é {} e seu sucessor é {}'.format(n, n-1, n+1))
except ValueError:
    sys.exit('Erro: Você digitou um valor inválido')