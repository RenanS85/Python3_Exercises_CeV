'''
EXERCÍCIO 004: Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
'''

algo = input('digite algo: ')
print ('Só tem espaços?: ', algo.isspace())
print ('qual tipo primitivo?','é uma', type(algo))
print ('é um número?', algo.isnumeric())
print ('é alfanumérico?', algo.isalnum())
print ('esta em maiusculo?', algo.isupper())
print ('esta em maiusculo?', algo.islower())
print ('Esta capitalizada?', algo.istitle())
