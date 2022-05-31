'''
EXERCÍCIO 080: Lista Ordenada sem Repetições
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []

for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c==0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista): #sempre que o numero for menor ou igual ele vai para a posição do numero atual
            lista.insert(pos,c)
            break
        pos+=1
print (f'Em ordem crescente: {lista}')
