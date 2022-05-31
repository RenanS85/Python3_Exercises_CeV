def leiaDinheiro(valor):
    while True:
        val = input(valor).replace(',','.').strip()
        try:
            f = float(val)
        except (ValueError,TypeError):
            print('ERRO - DIGITE UM VALOR VÁLIDO')
            continue
        else:
            break
    return f
