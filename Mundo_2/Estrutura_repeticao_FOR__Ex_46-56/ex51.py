'''
EXERCÍCIO 051: Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

#minha resolução 1
primeiro = (int(input('Digite o primeiro numero da PA: ')))
razao_pa = (int(input('Digite a razao da PA: ')))
ultimo = primeiro + (10 - 1) * razao_pa

for n in range (primeiro,ultimo+1,razao_pa):
    print(n,end=' ')

