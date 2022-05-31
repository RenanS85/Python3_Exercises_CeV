def leiaDinheiro(valor):
    val = input(valor).replace(',','.').strip()
    while True:
        if val == '' or val.isalpha()==True:
            val = input('Erro - DIGITE UM VALOR: ').replace(',','.').strip()
        else:
            return float(val)

def leiaInt(valor):
    while True:
        try:
            val = int(input(valor))
        except (ValueError,TypeError):
            print ('ERRO = DIGITE UM NUMERO INTEIRO')
            continue
        else:
            return val


def leiaFloat (valor):
    while True:
        try:
            val = float(input(valor))
        except (ValueError,TypeError):
            print ('ERRO = DIGITE UM NUMERO INTEIRO')
            continue
        else:
            return val







