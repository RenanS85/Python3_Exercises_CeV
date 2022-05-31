'''
EXERCÍCIO 087: Mais Sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um numero para [{l},{c}] '))
cont=0
sp=0
s=0
maior=0
for l in range (0,3):
    for c in range (0,3):
        print (f'[  {matriz[l][c]}  ]',end='')

        if matriz [l][c] %2==0:
            sp+=matriz [l][c]
    print()
for num in matriz[2]:
    s+=num
    matriz[1].sort()
    maior = matriz[1][2]

print (f'A soma dos pares é {sp}')
print (f'A soma da 3a linha é {s}')
print (f'O maior numero da segunda linha é {maior}')
