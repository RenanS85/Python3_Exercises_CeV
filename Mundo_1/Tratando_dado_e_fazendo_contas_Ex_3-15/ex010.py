'''
EXERCÍCIO 010: Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 4,72
'''
cot = 4.72
print ('Quantos dólares vc pode comprar com x reais')
ver = input ('deseja ver a cotação do dolar primeito? [S/N]: ').upper().strip()
if ver == 'S':
    print('a cotação é de R$ 4,72')
d = (float(input('quantos reais você tem?: ')))
print (f'Ok, com {d} reais vc consegue comprar {d/cot:.2f} dólares')