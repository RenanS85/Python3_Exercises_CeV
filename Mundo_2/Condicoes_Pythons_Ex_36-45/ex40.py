'''
EXERCÍCIO 040: Aquele Clássico da Média
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

import statistics

c=1
notas = []
for n in range (3):
    n = (float(input(f'Nota {c}:')))
    notas.append(n)
    c+=1

media = statistics.mean(notas)
print (f'sua media é {media:.2f}')

if media < 5:
    print ('reprovado')
elif media < 5 or media < 6.9:
    print ('recuperação')
elif media >= 7:
    print ('aprovado papai')



