'''
EXERCÍCIO 037: Conversor de Bases Numéricas
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecima
'''

o1 = 'Binário'
o2 = 'Hexadecimal'
o3 = 'Octogonal'

n = (int(input('digite um numero: ')))

c=1
for n in range (3):
    if c == 1:
        print (f'opção {c} - {o1}')
        c+=1
    elif c == 2:
        print(f'opção {c} - {o2}')
        c += 1
    elif c == 3:
        print(f'opção {c} - {o3}')

escolha = (int(input('Digite o numero da opção: ')))

n_binario = bin(n)
n_hexadec = hex(n)
n_octogo = oct(n)

if escolha == 1:
    print ('o numero em binario é', n_binario[2:])
elif escolha == 2:
    print ('o numero em hexadecimal é', n_hexadec[2:])
elif escolha == 3:
    print ('o numero em octogonal é', n_octogo[2:])

