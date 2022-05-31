'''
EXERCÍCIO 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    c=1
    n = float(input('vc quer ver a tabuada de qual valor: '))
    while c <=10 and n >= 0:
        print (f'{n} X {c} = {n*c}')
        c+=1
    if n < 0:
        break


