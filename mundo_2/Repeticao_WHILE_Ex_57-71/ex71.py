'''
EXERCÍCIO 071: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

def decoracao(txt):
    deco = '*'
    print(f'\033[43m{deco * 46}\033[m')
    print(f'\033[1;40m====( {txt} )==== \033[m')
    print(f'\033[43m{deco * 46}\033[m')

decoracao('SEJA BEM VINDO AO BANCO DO PYTHON')
print (f'Notas disponiveis:\nR${50.00}\nR${20.00}\nR${10.00}\nR${1.00}')
saque = int(input('DIGITE O VALOR QUE DESEJA SACAR: '))
total = saque
dic = {}
dic['notas de 50'] = 0
dic['notas de 20'] = 0
dic['notas de 10'] = 0
dic['notas de 01'] = 0
while True:
    if total>=50:
        total -= 50
        dic['notas de 50'] += 1
    elif total>=20:
        total -= 20
        dic['notas de 20'] += 1
    elif total>=10:
        total -= 10
        dic['notas de 10'] += 1
    elif total>=1:
        total -= 1
        dic['notas de 01'] += 1
    if total == 0:
        break

for k,v in dic.items():
    if v !=0:
        print (f'{v} {k}')







