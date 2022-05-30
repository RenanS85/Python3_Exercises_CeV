'''
EXERCÍCIO 003: Somando Dois Números
Crie um programa que leia dois números e mostre a soma entre eles.
'''

n1 = (float (input ('digite um número: ')))
n2 = (float (input('digite outro número: ')))
s = n1+n2
print ('o número {}, somado ao número {} é igual a {}'.format(n1,n2,s))

'''
##########################################
Para exibir outras operações como exemplo
##########################################
'''
p = n1*n2
d = n1/n2
print ('o número {}, multiplicado por {} é igual a {}'.format(n1,n2,p))
print ('o número {}, dividido pelo número {} é igual a {}'.format(n1,n2,d))
