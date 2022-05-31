'''
EXERCÍCIO 055: Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

lista = []
for pessoa in range (1,6):
        peso = (float(input('DIGITE seu peso (pessoa numero {}?: '.format(pessoa))))
        lista.append(peso)

lista_organizada = sorted(lista)
mais_pesado = max(lista)
mais_leve = min(lista)

print (f'A pessoa mais pesada, pesa {mais_pesado}kg, '
       f'enquanto a pessoa mais leve pesa {mais_leve}kg')



