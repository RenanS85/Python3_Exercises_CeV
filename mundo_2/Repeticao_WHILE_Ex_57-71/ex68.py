'''
EXERCÍCIO 068: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
'''

from random import randint

print ('-=-'*10)
print ('JOGO DO PAR OU IMPAR')
print ('-=-'*10)
c = 0

while True:
    n = int(input('Escolha seu numero, jovem: '))
    escolha = input('Voce quer par ou impar [P/I]: ').strip().upper()
    npc = randint(0,10)
    escolhapc= ''
    soma = n + npc
    c+=1
    venceu =''
    if escolha in 'Pp':
        escolhapc = 'Impar'
        escolha = 'Par'
    if escolha in 'Ii':
        escolhapc = 'Par'
        escolha = 'Impar'
    if escolha in 'Par' and soma%2 ==0:
        venceu = 'sim'
        print (f'A soma entre {n} e {npc} é {soma} que é {escolha}, so YOU WIN')
        print ('AGAIN!')
    elif escolha in 'Impar' and soma % 2 != 0:
        venceu = 'sim'
        print(f'A soma entre {n} e {npc} é {soma} que é {escolha}, so YOU WIN')
        print('AGAIN!')
    else:
        venceu = 'não'
        print (f'Eu escolhi {npc} e a soma com {n} é {soma} que é {escolhapc} ')
        print('YOU LOSE')
        break

print (f'voce ganhou {c-1} vezes')



