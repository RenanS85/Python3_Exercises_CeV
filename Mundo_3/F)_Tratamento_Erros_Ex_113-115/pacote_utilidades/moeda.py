def dobro (n,form=0):
    if form==0:
        return n*2
    elif form == True:
        return (f'R$ {n*2:.2f}').replace('.',',')


def metade (n,form=0):
    if form ==0:
        return n/2
    elif form == True:
        return (f'R$ {n/2:.2f}').replace('.',',')


def perc_aument (pre,aum,form=0):
    if form == 0:
        return pre+(pre*(aum/100))
    elif form == True:
        return (f'R$ {pre+(pre*(aum/100)):.2f}').replace('.',',')

def perc_diminui (pre,aum,form=0):
    if form == 0:
        return pre-(pre*(aum/100))
    elif form == True:
        return (f'R$ {pre-(pre*(aum/100)):.2f}').replace('.',',')

def moeda (pre):
    return (f'R$ {pre:.2f}').replace('.',',')

def resumo (pre,aum,dim):
    print ('-~'*20)
    print ('TABELA DE RESUMO'.center(40))
    print('-~' * 20)
    print(f'Preço analisado: \t{moeda(pre):>}')
    print (f'Dobro do preço: \t{dobro(pre,True):>}')
    print (f'Metade do preço: \t{metade(pre,True):>}')
    print (f'Aumentando {aum}%: \t{perc_aument(pre,aum,True):>}')
    print (f'Diminuindo {dim}%: \t{perc_diminui(pre,aum,True):>}')