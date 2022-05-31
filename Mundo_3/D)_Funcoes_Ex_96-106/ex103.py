'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido informado corretamente.

'''

def ficha (j=0,g=0):
    if j != 0 and g !=0:
        print (f'O jogador {j} fez {g} gols')
    elif j!=0 and g ==0:
        print (f'O jogador {j} fez 0 gols')
    elif j==0 and g !=0:
        print (f'O jogador <desconhecido> fez {g} gols')
    elif j==0 and g ==0:
        print (f' O jogador <desconhecido> fez 0 gols')


jogador = str(input('Nome do Jogador: '))
gol = str(input('Numero de Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jogador.strip()=='':
    jogador=0

ficha(jogador,gol)