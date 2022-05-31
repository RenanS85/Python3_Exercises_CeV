'''
EXERCÍCIO 088: Palpites Para a Mega Sena
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

def mensagem (msg):
    print('=-'*30)
    print ('{:^60}'.format(msg))
    print ('=-'*30)
    print (' ')
def gera_n_jogos ():
    from random import randint
    lista_n_jogos = list()
    for jogos in range (1,n_jogos+1):
        lista_n_jogos.append([])
    for j in lista_n_jogos:
        while len(j) < 6:
            num = randint(1,60)
            while num not in j:
                j.append(num)
    c=1
    for j in  lista_n_jogos:
        print (f'Jogo numero {c}: {j}')


mensagem('GERADOR DE MEGA SENA')
n_jogos = int(input('Quantos jogos vc deseja gerar?: '))
gera_n_jogos()


