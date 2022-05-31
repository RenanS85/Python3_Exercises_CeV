'''
EXERCÍCIO 036: Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
'''

import math

print ('você quer um empréstimo, ok, vamos lá')
valor_casa = (float(input('Qual é o valor da casa?: ')))
valor_salario = (float(input('Qual seu salário?: ')))
anos_pagamento = (float(input('em quantos anos você vai pagar?: ')))

meses_pagamento = anos_pagamento*12
valor_prestacao = (valor_casa/(meses_pagamento))

if valor_prestacao > (valor_salario*0.30):
    print ('Seu empréstimo foi negado')
else:
    print ('ok, faremos o empréstimo')

print (f'a casa sera parcelada em {math.floor(meses_pagamento)} '
       f'vezes e o valor de cada parcela é {valor_prestacao:.2f}')
