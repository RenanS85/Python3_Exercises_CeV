'''
EXERCÍCIO 057: Validação de Dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = input('Digite seu sexo: ').strip().upper() [0]
while sexo not in 'mfMF':
    sexo = input('tente novamente: ').strip().upper() [0]
print ('ok, validado')

