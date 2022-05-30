'''
EXERCÍCIO 025: Procurando uma String Dentro de Outra
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = input('digite seu nome: ').lower()
if 'silva' in nome:
    print ('tem silva')
else:
    print ('não tem silva')

