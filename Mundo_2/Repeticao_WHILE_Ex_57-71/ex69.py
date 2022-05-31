'''
EXERCÍCIO 069: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
'''

idades = []
homens = []
mulheres = []
maiores = []
c=1
while True:
        nome = input(f'Nome da pessoa {c}:').title().strip()
        idade = int(input(f'Idade da pessoa {c}: '))
        sexo =  input(f'Sexo da pessoa {c}: ').upper()
        idades.append(idade)
        if idade > 18:
            maiores.append(idade)
        if sexo == 'M':
            homens.append(idade)
        elif sexo == 'F':
            mulheres.append(idade)
        idades.append(idade)
        continua = input('CADASTRAR MAIS PESSOAS? [S/N]').upper().strip()
        if continua == 'S':
            c += 1
        else:
            break

n_homens = len(homens)
menos_20 = len(mulheres)

print(f'A) Quantas pessoas têm mais de 18 anos: {len(maiores)}')
print(f'B) Quantos homens foram cadastrados: {n_homens}')
print(f'C) Quantas mulheres têm menos de 20 anos: {menos_20}')














