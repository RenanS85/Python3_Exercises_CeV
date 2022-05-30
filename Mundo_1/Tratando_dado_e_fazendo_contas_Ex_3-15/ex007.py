'''EXERCÍCIO 007: Média Aritmética
Desenvolva um programa que leia 4 notas de um aluno, calcule e mostre a sua média.

OBS: Modificado para ler 4 notas

A leitura das notas pode ser feita em um laço FOR...
'''

print('a seguir digite suas nota de 0 a 10')
n1 = (float(input ('qual sua nota na 1a prova?')))
n2 = (float(input ('qual sua nota na 2a prova?')))
n3 = (float(input ('qual sua nota na 3a prova?')))
n4 = (float(input ('qual sua nota na 4a prova?')))
print ('Coloquei no código formas diferentes')

'''RESOLUÇÂO 1'''

listadenotas = [n1,n2,n3,n4]
print ('a média é',sum(listadenotas)/len(listadenotas))

'''RESOLUÇÂO 2
aqui eu importei a biblioteca statistics uma das que conterm a funçao mean, de média'''

import statistics
print ('a média das notas é', statistics.mean(listadenotas))
