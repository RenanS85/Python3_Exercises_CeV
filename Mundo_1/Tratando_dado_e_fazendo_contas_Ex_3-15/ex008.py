"""
EXERCÍCIO 008: Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

print('escolher um valor em metros e converter para cm e mm')
n = (float(input('Digite seu número em metros')))
print('a conversão fica; {:.3f}cm e {:.3f}m'.format(n/100, n/1000))