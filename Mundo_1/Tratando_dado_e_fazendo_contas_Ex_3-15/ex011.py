'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
'''

print ('vamos descobrir a quantidade de tinta para pintar sua parede!')
h = (float(input('qual a altura da sua parede?: ')))
l = (float(input('qual a largura da sua parede?: ')))
sabermais = input('vocÊ quer saber quantos litros de tinta se gastam por m²?: [S/N]').upper().strip()
if sabermais == 'S':
    print ('cada 0,5 litros de tinta pintam 1m², ou seja, 1 litro de tinta faz 2m²')
print(f'para sua parede serão necessários {h*l/2} litros de tinta')

