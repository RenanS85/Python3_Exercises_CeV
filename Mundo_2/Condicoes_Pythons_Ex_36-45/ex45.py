'''
EXERCÍCIO 045: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.
'''

escolha = (str(input('Escolha pedra, papel ou tesoura: '))).strip()
from random import choice
lista_pc = ['pedra','papel','tesoura']
pc_escolhe = choice(lista_pc)
print ('o pc escolheu...')
from time import sleep
sleep(2)
print ('\033[1;30;41mJO \033[m')
sleep(2)
print ('\033[1;30;41mKEN \033[m')
sleep(2)
print (f'\033[1;30;41mP{"O"*6} \033[m')
sleep(2)
print ('O pc escolheu', pc_escolhe)

if escolha == 'pedra' and pc_escolhe == 'papel':
    print ('você perdeu')
elif escolha == 'pedra' and pc_escolhe == 'tesoura':
    print ('você ganhou')
elif escolha == 'papel' and pc_escolhe == 'pedra':
    print('você ganhou')
elif escolha == 'papel' and pc_escolhe == 'tesoura':
    print ('você perdeu')
elif escolha == 'tesoura' and pc_escolhe == 'pedra':
    print ('você perdeu')
elif escolha == 'tesoura' and pc_escolhe == 'papel':
    print ('você ganhou')
elif escolha == pc_escolhe:
    print ('empate')



