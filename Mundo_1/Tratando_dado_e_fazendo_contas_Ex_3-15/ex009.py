'''
EXERCÍCIO 009: Tabuada
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''

print ('exercicio 9 : fazer a tabuada de algum número')
n = (int(input('Escolha seu número: ')))
numeros = [1,2,3,4,5,6,7,8,9,10]
print ('-'*17)
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[0],n,n*numeros[0]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[2],n,n*numeros[2]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[3],n,n*numeros[3]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[4],n,n*numeros[4]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[5],n,n*numeros[5]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[6],n,n*numeros[6]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[7],n,n*numeros[7]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[8],n,n*numeros[8]))
print('  {:>2} x {:>2} = {:>2}  '.format(numeros[9],n,n*numeros[9]))
print ('-'*17)



