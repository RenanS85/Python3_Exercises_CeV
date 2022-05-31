'''
EXERCÍCIO 093: Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

class Jogador:
    def __init__(self, nome,partidas):
        self.nome = nome
        self.partidas = partidas
        self.gols = {}

nome = input('Nome')
partidas = int(input('Partidas'))
jogador = Jogador(nome,partidas)
for p in range (partidas):
    gols = int(input(f'Gols na partida {p+1}'))
    jogador.gols[f'p{p+1}'] = gols
print('')
c=1
for k,v in jogador.__dict__.items():
    if k != 'gols':
        print (f'{k} --> {v}')
    else:
        for v in jogador.gols.values():
            print (f'Partida {c} = {v} gols')
            c+=1

