'''
EXERCÍCIO 065: Maior e Menor Valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
'''
from statistics import mean

status = True
list = []
while status:
    quant = int(input('Quantos número quer ler?: '))
    for c in range (1,quant+1):
        n = float(input(f'Digite o {c} número: '))
        list.append(n)
    med = mean(list)
    sort = sorted(list)
    maior = sort[len(sort)-1]
    menor = sort[0]
    print (f'a média aritmética dos umeros é {med}')
    print (f'o maior numero foi {maior}')
    print (f'o menor numero foi {menor}.')
    continua = input('Deseja adicionar mais números? [S/N]').upper().strip()
    if continua == 'S':
        pass
    else:
        status = False







