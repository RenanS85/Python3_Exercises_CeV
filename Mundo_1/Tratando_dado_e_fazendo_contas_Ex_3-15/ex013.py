'''
EXERCÍCIO 013: Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com uma % de aumento

OBS: Exercício modificado, pois o original define 15% de aumento.
'''

def f_preco(preco):
    x = f'{preco:.2f}'
    p = str(x).replace('.',',')
    return f'R$ {p}'


print('Quanto ganho com um aumento no trabalho?')
salario = (float(input('Qual seu salário?: ')))
aumento = (float(input('qual é a porcentagem do seu aumento? DIGITE APENAS NÚMEROS: ')))
valoraumento = (salario*(aumento/100))
novosalario = (salario+valoraumento)
print('Seu aumento será de:', f_preco(valoraumento))
print ('Seu novo salário será de:', f_preco(novosalario) )
