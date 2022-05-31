def dobro (n,form=False):
    d = n*2
    if form:
        return formata(d)
    else:
        return d

def metade (n,form=False):
    m = n/2
    if form:
        return formata(m)
    else:
        return m

def perc_aument (pre,aum,form=0):
    amt = pre+((aum/100)*pre)
    if form:
        return formata(amt)
    else:
        return amt

def perc_diminui (pre,dmn,form=0):
    dmn = pre + ((dmn / 100) * pre)
    if form:
        return formata(dmn)
    else:
        return dmn

def formata (pre):
    return (f'R$ {pre:.2f}').replace('.',',')

def resumo (pre,aum,dim):
    print ('-~'*20)
    print ('TABELA DE RESUMO'.center(40))
    print('-~' * 20)
    print(f'Preço analisado: \t{formata(pre):>}')
    print (f'Dobro do preço: \t{dobro(pre,True):>}')
    print (f'Metade do preço: \t{metade(pre,True):>}')
    print (f'Aumentando {aum}%: \t{perc_aument(pre,aum,True):>}')
    print (f'Diminuindo {dim}%: \t{perc_diminui(pre,aum,True):>}')