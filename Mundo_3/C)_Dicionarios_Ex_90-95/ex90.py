'''
EXERCÍCIO 090: Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}
aluno['nome']=(input('Nome: ')).title().strip()
aluno['média']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] < 5:
    aluno['situação']='Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print (f'o aluno de nome {aluno["nome"]} teve a média de {aluno["média"]} e esta {aluno["situação"]}')


