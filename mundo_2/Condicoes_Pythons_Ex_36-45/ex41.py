'''
EXERCÍCIO 041: Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTE
'''

from datetime import date

ano_nascimento = (int(input('Ano nascimento: ')))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

#categorias até:
mirim = 9
infantil = 14
junior = 19
senior = 20

if idade <= 9:
    print ('mirim')
elif idade <= 14:
    print ('infantil')
elif idade <= 19:
    print ('junior')
elif idade <= 20:
    print ('senior')
elif idade > 20:
    print ('master')





