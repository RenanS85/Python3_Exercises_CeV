'''
EXERCÍCIO 032: Ano Bissexto
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

ano = (int(input('digite um ano: ')))
if ano%4 == 0:
    print ('é ano bissexto')
else:
    print ('nao é ano bissexto')
