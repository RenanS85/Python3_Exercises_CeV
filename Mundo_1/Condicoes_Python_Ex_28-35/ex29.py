'''
EXERCÍCIO 029: Radar Eletrônico
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
'''

for veloc in range (10, 110, 10):
    veloc

import random
vel = random.randrange(veloc)

print ('limte de velocidade de 80km/h')
print ('o carro passou no radar a {}km/h'.format(vel))

if vel > 80:
    multa = ((vel-80)*7)
    print ('vc estava a {}km/h, {} acima do permitido, sua multa é de R$ {:.2f}'.format(vel,vel-80,multa))
if vel <= 80:
    print ('vc estava a {}, esta tudo certo, sem multa'.format(vel))