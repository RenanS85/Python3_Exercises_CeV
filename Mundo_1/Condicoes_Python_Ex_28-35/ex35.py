'''
EXERCÍCIO 035: Analisando Triângulo v1.0
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''



r1 = float(input('1º LADO: '))
r2 = float(input('2° LADO: '))
r3 = float(input('3° LADO: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')