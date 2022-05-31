'''
Exercício Python 102: Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial (n,show=False):
    """
    :param n: numero para calculo
    :param show: mostrar ou não as contas
    :return: resultado do fatorial
    """
    f=1
    for c in range (n,0,-1):
        f*=c
        if show  and c > 1:
            print(f'{c} X ',end='')
        if show and c <= 1:
            print (f'{c} = ',end='')
    return f
print(fatorial(5))
print(fatorial(5,show=True))

