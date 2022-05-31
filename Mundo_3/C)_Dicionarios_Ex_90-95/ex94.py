'''
EXERCÍCIO 094: Unindo Dicionários e Listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
'''
from abc import ABC
from statistics import mean
class Pessoa(ABC):
    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class Homem(Pessoa):
    pass

class Mulher(Pessoa):
    pass

idades = []
pessoas = []
homens = []
mulheres = []
while True:
    nome = input('Nome: ').title().strip()
    idade = int(input('Idade '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    if sexo == 'M':
        homem = Homem(nome,idade,sexo)
        homens.append(homem.__dict__)
        pessoas.append(homem.__dict__)
    elif sexo == 'F':
        mulher = Mulher(nome,idade,sexo)
        mulheres.append(mulher.__dict__)
        pessoas.append(mulher.__dict__)
    idades.append(idade)
    continua = input('CADASTRAR MAIS PESSOAS? [S/N]').upper().strip()
    if continua == 'N':
        break

print (f'{len(pessoas)} cadastradas')
print (f'A média de idade é {mean(idades)}')
print(f'Lista de homens:\n{homens}')
print('')
print(f'Lista de mulheres:\n{mulheres}')



