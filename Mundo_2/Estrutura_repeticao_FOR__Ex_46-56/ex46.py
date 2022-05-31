'''
EXERCÍCIO 046: Contagem Regressiva
Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep
print ('vamos soltar fogos de artificio!')

for contagem in range (10,0,-1):
    sleep(0.5)
    print (contagem)

sleep(0.2)

c=1
for o in range (10):
    if c == 1:
        print ('B',end='')
        c+=1
    elif 1 < c < 10:
        sleep(0.1)
        print ('O',end ='')
        c+=1
    elif c == 10:
        print ('M', end = '')


