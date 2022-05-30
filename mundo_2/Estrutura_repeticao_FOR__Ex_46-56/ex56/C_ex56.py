'''EXERCÍCIO 056: Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.'''

from statistics import mean
from B_classes_ex56 import Homem,Mulher

idades = []
homens = []
mulheres = []
c=1
for n in range (5):
    nome = input(f'Nome da pessoa {c}:').title().strip()
    idade = int(input(f'Idade da pessoa {c}: '))
    sexo =  input(f'Sexo da pessoa {c}: ').upper()
    if sexo == 'M':
        homem = Homem(nome,idade,sexo)
        homens.append(homem.__dict__)
    elif sexo == 'F':
        mulher = Mulher(nome,idade,sexo)
        mulheres.append(mulher.__dict__)
    idades.append(idade)
    c+=1

media = mean(idades)
print (f'A média de idade é: {media}')
sort = sorted(homens,key=lambda k: k['idade'],reverse=True)
homem_velho = sort[0]['nome']
print(f'O homem mais velho se chama {homem_velho}')

c=0
for mulher in mulheres:
    if mulher['idade'] < 20:
        print (f'a {mulher["nome"]} tem menos de 20 anos')
        c+=1
print(f'São {c} mulheres com menos de 20 anos')














