'''
EXERCÍCIO 054: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

import datetime
data_atual = datetime.date.today().year
maioridade = 18
c1 = 0
c2 = 0
for ano in range (1,8):
    nascimento = (int(input('Qual ano a {}ª pessoa nasceu: '.format(ano))))
    if (data_atual - nascimento) < maioridade:
        c1 += 1
    if (data_atual - nascimento) >= maioridade:
        c2 += 1

print ('{} pessoas ainda são menores e {} pessoas já são maiores'.format(c1,c2))






