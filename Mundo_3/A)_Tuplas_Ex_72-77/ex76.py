'''
EXERCÍCIO 076: Lista de Preços com Tupla
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

prods = ('Coca-Cola',1.00,'Heineiken Lata',6.00,'Cheetos',4.00,'Gelo',8.00)
n=0
print('=-'*19)
for a in range (0,len(prods)-1):
    print (f'{prods[n]:.<30} R$ {prods[n+1]:.2f}')
    n+=2
    if n >= len(prods)-1:
        break
print('=-'*19)

