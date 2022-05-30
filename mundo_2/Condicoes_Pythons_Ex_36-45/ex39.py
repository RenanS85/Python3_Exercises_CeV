'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
ano_nascimento = (int(input('Qual o ano de seu nascimento: ')))
ano_atual = date.today().year
idade_alistamento = 18

if (ano_atual - ano_nascimento) == idade_alistamento:
    print ('voce tem {} é hora de alistar'.format(ano_atual - ano_nascimento))
elif (ano_atual - ano_nascimento) < idade_alistamento:
    print ('voce tem {}, ainda não é hora de se alistar'.format(ano_atual-ano_nascimento))
elif (ano_atual - ano_nascimento) > idade_alistamento:
    print ('Voce tem {}, ja passou da hora de se alistar'.format(ano_atual-ano_nascimento))

if (ano_atual - ano_nascimento) < idade_alistamento:
    print ('faltam {} anos para seu alistamento, voce deve se alistar em {}'
           .format(idade_alistamento - (ano_atual-ano_nascimento),ano_atual+idade_alistamento - (ano_atual-ano_nascimento)))
elif (ano_atual - ano_nascimento) > idade_alistamento:
    print('ja se passaram {} anos para seu alistamento, voce deveria ter'
          ' se alistado em {}'.format(ano_atual-(ano_nascimento+idade_alistamento),ano_nascimento+idade_alistamento))

