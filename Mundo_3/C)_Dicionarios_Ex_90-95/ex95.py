'''
EXERCÍCIO 095: Aprimorando os Dicionários
Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

class Jogador:
    def __init__(self, nome,partidas):
        self.nome = nome
        self.partidas = partidas
        self.gols = {}
        self.aproveitamento = 0

jogadores = {}
cont = 1
tot = 0
while True:
    nome = input('Nome')
    partidas = int(input('Partidas'))
    jogador = Jogador(nome,partidas)
    for p in range (partidas):
        gols = int(input(f'Gols na partida {p+1}'))
        jogador.gols[f'p{p+1}'] = gols
        tot += gols
    jogador.aproveitamento = tot/partidas
    jogadores[f'jogador{cont}'] = jogador.__dict__
    continua = input('CADASTRAR MAIS JOGADORES? [S/N]').upper().strip()
    cont+=1
    if continua == 'N':
        break

print(jogadores)
print('')

for v in jogadores.values():
    for values,keys in v.items():
        print(values,keys)
    print('')
