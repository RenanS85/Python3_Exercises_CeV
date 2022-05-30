'''
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''

n = input("digite seu nome: ").title()
nome = n.split()
print ('Seu primeiro nome é:', nome[0])
print ('Seu ultimo nome é:', nome[len(nome)-1])