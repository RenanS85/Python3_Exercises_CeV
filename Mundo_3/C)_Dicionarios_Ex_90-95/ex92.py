'''
EXERCÍCIO 092: Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date
dados = {}
dados['nome']=input('Nome: ')
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
dados['idade']=ano_atual-nascimento
dados['ctps']=int(input('Carteira de Trabalho (0 se não tem): '))
if dados['ctps'] != 0:
    dados['ano contratação']=int(input('Ano de contratação: '))
    dados['Salário']=int(input('Salário: '))
print(dados)
for k,v in dados.items():
    print (f'O {k} tem o valor de {v}')
    if dados['ctps']!=0:
        if ano_atual - dados['ano contratação'] == 35:
            print (f'você pode se aposentar esse ano')
    elif dados['ctps']!=0:
        if ano_atual - dados['ano contratação'] > 35:
            print (f'ja faz {(35-(ano_atual - dados["ano contratação"]))*-1} anos que vc pode se aposentar')
