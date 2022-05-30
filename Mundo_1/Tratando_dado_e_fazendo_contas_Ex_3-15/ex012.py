'''EXERCÍCIO 012: Calculando Descontos
ORIGINAL:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

RESOLUÇÃO REALIZADA COM DESCONTO ESCOLHIDO PELO USUÁRIO.
'''

def f_preco(preco):
    x = f'{preco:.2f}'
    p = str(x).replace('.',',')
    return f'R$ {p}'

print('vamos ver o preço de um produto com desconto')
preco = (float(input('Qual preço do seu produto na venda?: ')))
desconto = float(input('Qual porcetagem de desconto deseja dar?\n'
                       'DIGITE SOMENTE O NÚMERO: '))
desc = preco*(desconto/100)
preco_desc = (preco - desc)
print (f'O valor original da venda é {f_preco(preco)} o desconto de {f_preco(desconto)}% corresnponde a {f_preco(desc)}\n'
       f'O VALOR FINAL COM DESCONTO É {f_preco(preco_desc)}')
