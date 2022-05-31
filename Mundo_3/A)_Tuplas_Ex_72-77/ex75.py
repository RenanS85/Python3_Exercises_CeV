'''
EXERCÍCIO 075: Análise de Dados em uma Tupla
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

list = []
for n in range (4):
    n = float(input('Digite um numero: '))
    list.append(n)
tupla = tuple(list)

print (f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print (f'O valor 3 apareceu primeiro na posição {tupla.index(3)}')
else:
    print ('o 3 nao apareceu')

c=0
for pares in tupla:
    if pares % 2==0:
        print (f'O {pares} é par')
        c+=1
print (c, 'numero são pares')




