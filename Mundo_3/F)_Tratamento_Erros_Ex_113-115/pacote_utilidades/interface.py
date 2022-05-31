def linha (tam=42):
    return '-'*tam

def cabecalho (txt):
    print (linha())
    print (txt.center(42))
    print (linha())

def menu (lista):
    cabecalho('Programa de cadastro v1.0')
    c=1
    for item in lista:
        print (f'{c} - {item}')
        c+=1
    print (linha())
    opc = leiaInt('Digite sua Opção: ')
    return opc

def leiaInt(valor):
    while True:
        try:
            val = int(input(valor))
        except (ValueError,TypeError):
            print ('ERRO = DIGITE UM NUMERO INTEIRO')
            continue
        else:
            return val