'''
EXERCÍCIO 059: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

def numeric_validation(txt, integer = False, range=None):
    """
    Valida inputs numéricos
    :param txt: Texto para receber input numérico.
    :param integer: Determina se o número será inteiro, se False recebe Float.
    :param range: Se int = True, range delimita o valor máximo a receber.
    :return: input de txt
    """
    while True:
        try:
            if integer and range:
                num = int(input(txt))
                if num < 1 or num > range:
                    continue
            else:
                num = float(input(txt))
        except (ValueError, TypeError):
            continue
        else:
            break
    return num

n1 = numeric_validation('Digite um número: ')
n2 = numeric_validation('Digite outro número: ')

while True:
    print(' Bem vindo! OQUE DESEJA FAZER?\n'
          '[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] Sair do Programa')
    resp = numeric_validation('SUA OPÇÂO:',integer=True,range=5)
    if resp == 1:
        s = n1+n2
        print(f'{n1} + {n2} = {s} ')
    elif resp == 2:
        m = n1 * n2
        print(f'{n1} X {n2} = {m} ')
    elif resp == 3:
        if n1>n2:
            print(f'{n1} > {n2}')
        else:
            print(f'{n2} > {n1}')
    elif resp == 4:
        n1 = numeric_validation('Digite um número: ')
        n2 = numeric_validation('Digite outro número: ')
    elif resp == 5:
        print ('Bye Bye :)')
        exit()


