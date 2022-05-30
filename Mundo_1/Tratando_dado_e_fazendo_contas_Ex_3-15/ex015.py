'''
EXERCÍCIO 015: Aluguel de Carros
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''

import sys

def f_preco(preco):
    x = f'{preco:.2f}'
    p = str(x).replace('.',',')
    return f'R$ {p}'

gostaria = input ('Voce gostaria de alugar um carro? [S/N]: ').strip().upper()
if gostaria == 'S':
    print ('ok, vou te passar os valores!')
else:
    sys.exit('OK, volte quando desejar alugar um veículo')

valor_dia = 60.00
valor_km = 0.15
print ('O valor por dia é', f_preco(valor_dia), 'já o valor por km é', f_preco(valor_km))
dias_alugados = (int(input ('Quantos dias vc vai alugar?: ')))
print ('ok, alugando por', dias_alugados, 'o valor fica {}'.format(f_preco(dias_alugados*valor_dia)))
km_rodados = (float(input('Quantos km tu girou?: ')))
print ('Ok, o valor total fica {}.'.format( f_preco((dias_alugados*valor_dia)+(km_rodados*valor_km))))

