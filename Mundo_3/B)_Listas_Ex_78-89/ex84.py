'''
EXERCÍCIO 084: Lista Composta e Análise de Dados
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.


Base para cálculos:
25 a 29 anos (médias):
Altura : 173,0 - 160,7
Peso:     72,7 - 60,5


'''

class Pessoa:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

def cadastro():
    while True:
        try:
            nome = input('Nome: ')
            peso = int(input('Peso: '))
        except (ValueError, TypeError):
            print ('ERRO - digite novamente')
            continue
        else:
            pessoa = Pessoa(nome,peso)
            break
    return pessoa.__dict__


pessoas = []
leves = []
pesados = []
while True:
    pessoa = cadastro()
    pessoas.append(pessoa)
    if 60.5 > pessoa['peso']:
        leves.append(pessoa)
    elif 72.7 < pessoa['peso']:
        pesados.append(pessoa)
    continua = input('Cadastrar mais pessoas? [S/N]').strip().upper()
    if continua == 'S':
        continue
    else:
        break
print (f'Foram cadastradas {len(pessoas)} pessoas')
print('Os mais pesados: ')
for pesado in pesados:
    for k,v in pesado.items():
        print (f'{k} : {v}')
print('')
print('Os mais leves: ')
for leve in leves:
    for k,v in leve.items():
        print (f'{k} : {v}')