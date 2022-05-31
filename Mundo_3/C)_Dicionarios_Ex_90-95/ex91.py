'''
EXERCÍCIO 091: Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint

class Jogador:
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero

lista = []
for c in range (4):
    nome = input(f'Nome do {c+1}º jogador: ')
    numero = randint(1,6)
    jogador = Jogador(nome,numero)
    lista.append(jogador.__dict__)

org = sorted(lista, key= lambda k : k['numero'], reverse=True)

for jogador in org:
    for k,v in jogador.items():
        print(f'{k} : {v}')
    print('')












