'''
EXERCÍCIO 003_modificado: Leia quantos números o usuário escolher,
imprima as operações de soma e o resultado ao final.
'''

x = int(input('Quantos números quer somar?'))
c=1
s=0
list = []
for cont in range (x):
    n = float(input(f'digite o {c}º número'))
    c+=1
    s+=n
    list.append(n)

c=1
for n in list:
    if c == len(list):
        print(f'{list[c - 1]} = {s}')
    else:
        print (f'{n} + ',end='')
        c+=1

