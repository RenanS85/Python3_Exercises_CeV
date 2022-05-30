'''
EXERCÍCIO 062: Super Progressão Aritmética v3.0
Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

primeiro_pa = (int(input('Digite o primeiro numero da PA: ')))
razao_2pa = (int(input('Digite a razao da PA: ')))
termo = primeiro_pa
cont = 1
total = 0
mais = 10
while mais != 0:
    total+=mais
    while cont <= total:
        print ('{} ->'.format(termo), end=' ')
        termo += razao_2pa
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos mais?: '))
print ('Você chegou a {} termos no total: '.format(total))









