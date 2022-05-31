'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
palavra 'FIM', o programa se encerrará. Importante: use cores.

OBS: Não criado com cores, redflag = "N".

'''
while True:
    help(input('Digite um comando: '))
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while continua not in 'SsNn':
        continua = str(input('DIGITE UMA OPÇÂO VÁLIDA - Quer continuar? [S/N]: ')).strip().upper()
    if continua in 'Nn':
        break




