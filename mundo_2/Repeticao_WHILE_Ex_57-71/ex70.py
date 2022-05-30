'''
EXERCÍCIO 070: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
'''

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

def decoracao():
    s = '**'
    print(f'\033[43m{s*20}\033[m')
carrinho = []
tot = 0
c = 0
while True:
    decoracao()
    nome = input('PRODUTO: ')
    preco = float(input('PREÇO R$ '))
    produto = Produto(nome,preco)
    carrinho.append(produto.__dict__)
    tot+=preco
    if preco > 1000:
        c+=1
    continua = input('Cadastrar mais produtos: [S/N]').upper().strip()
    if continua == 'S':
        pass
    else:
        break

org = sorted(carrinho, key=lambda k: k['preco'])

print ('')
print (f'Total: R$ {tot}')
print (f'O produto mais barato é {org[0]["preco"]}')
print (f'{c} produtos custam mais de MIL REAIS')
