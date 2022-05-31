'''
EXERCÍCIO 044: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

preco_prod = (float(input('Dgite o preço do produto: R$: ')))
form_pgmt = (int(input('Escolha a forma de pagamento:'
'\n DIGITE 1 para pagamento a com dinheito'
'\n DIGITE 2 para cartão de crédito'
'\nForma de pagameanto: ')))

preco_dinheiro = preco_prod - (preco_prod * 0.10)
preco_cartaoavista = preco_prod - (preco_prod * 0.05)
preco_parc2x = preco_prod
preco_parc_maisde2x = preco_prod + (preco_prod * 0.20)

if form_pgmt == 1:
    print ('O valor é {:.2f}, no dinheiro'.format(preco_dinheiro))

if form_pgmt == 2:
    vai_parcelar = (int(input('Selecione a forma de parcelamento:'
    '\n DIGITE 1 para cartão de crédito a vista'
    '\n DIGITE 2 para parcelar'
    '\n FORMA DE PAGAMENTO: ')))

if form_pgmt == 2 and vai_parcelar == 1:
    print ('O valor é {:.2f}, no crédito a vista'.format(preco_cartaoavista))

if form_pgmt ==2 and vai_parcelar == 2:
    numero_parcelas = (int(input('Selecione o numero de parcelas'
    '\nentre 2 e 12'
    '\n DIGITE O NÚMERO DE PARCELAS: ')))
if numero_parcelas > 12:
    print ('Não é possivel parcelar em mais de 12 vezes')
    exit()

if numero_parcelas == 2:
    print ('O valor é {:.2f}, em 2 parcelas de {:.2f}'.format(preco_parc2x, preco_parc2x / 2))
elif numero_parcelas > 2:
    print ('O valor é {:.2f}, em {} parcelas de {:.2f}'.format(preco_parc_maisde2x, numero_parcelas, preco_parc_maisde2x / numero_parcelas))

