from time import sleep
from pacote_utilidades.moeda import *
from pacote_utilidades.dados import leiaDinheiro

p = leiaDinheiro('Preço do produto: ')
print (f'Ok, vamos formatar {p}')
sleep(1)
print (f'Usando a função formata fica assim: {formata(p)}')
sleep(1)
aum = float(input('Escolha uma % de aumento para o valor: '))
dmn = float(input('Escolha uma % de diminuição para o valor: '))
sleep(1)
print(f'Aumentando {aum}% o preço sem formatar é {perc_aument(p,aum)}\n'
      f'para formatar basta coloar form = True no parâmetro da função formata: {perc_aument(p,aum,form=True)}')
print (f'Diminuindo {dmn}% o preço é {perc_diminui(p,dmn,form=True)}')
sleep(1)
print (f'O dobro do preço é {dobro(p,form=True)}, a metade é {metade(p,form=True)}')
sleep(1)
resumo(p,aum,dmn)







