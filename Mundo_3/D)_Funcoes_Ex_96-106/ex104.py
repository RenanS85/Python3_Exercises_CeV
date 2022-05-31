'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiInt(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok=True
        else:
            print ('ERRO, digite um numero inteiro valido: ')
        if ok == True:
            break
    return valor


n = leiInt('Digite um numero: ')
print (f'vc digitou o numero {n}')