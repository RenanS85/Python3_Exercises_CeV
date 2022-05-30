'''
EXERCÍCIO 031: Custo da Viagem
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
'''

dist = (float(input('Digite a distância da viagem: ')))
if dist <= 200:
    print ('a passagem é {:.2f}'.format(dist*0.5))
else:
    print ('a passagem é {:.2f}'.format(dist*0.45))