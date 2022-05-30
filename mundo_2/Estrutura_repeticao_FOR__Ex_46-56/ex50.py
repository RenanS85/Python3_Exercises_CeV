'''
EXERCÍCIO 050: Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

s=0
for numeros in range (1,7):
    n = (int(input('Digite o {} numero: '.format(numeros))))
    if n %2 == 0:
        print (n, 'é par, entao entra na jogada')
        print ('-=-'*15)
        s += n
    else:
        print (n, 'é impar e não sera considerado')
        print('-=-' * 15)
print ('')
print ('a soma de todos os paraes é', s)
