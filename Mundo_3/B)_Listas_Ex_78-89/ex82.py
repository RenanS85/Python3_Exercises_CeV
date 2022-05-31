'''
EXERCÍCIO 082: Dividindo Valores em Várias Listas
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.
'''

lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    quer = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while quer not in 'SsNn':
        quer = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if quer in 'Nn':
        break
listapar = []
listaimpar = []
for valores in lista:
    if valores %2==0:
        listapar.append(valores)
    else:
        listaimpar.append(valores)
print (f' {lista} --> Lista Completa')
print (f' {lista} --> Pares')
print (f' {listaimpar} --> Impares')