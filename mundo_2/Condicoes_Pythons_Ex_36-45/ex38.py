'''
EXERCÍCIO 038: Comparando Números
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
'''

n1 = (int(input('Digite um um número inteiro: ')))
n2 = (int(input('Digite outro número inteiro: ')))

if n1 > n2:
    print ('o primeiro numero é maior que o segundo')
elif n2 > n1:
    print ('o segundo numero é maior que o primeiro')
else:
    print ('os dois numeros são iguais')