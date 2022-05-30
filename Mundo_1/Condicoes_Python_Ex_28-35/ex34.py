'''
EXERCÍCIO 034: Aumentos Múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
'''

sal = (float(input('Qual seu salário: ')))
if sal > 1250:
    print ('seu novo salario é: {}'.format(sal+(sal*0.10)))
else:
    print('seu novo salario é: {}'.format(sal + (sal * 0.15)))