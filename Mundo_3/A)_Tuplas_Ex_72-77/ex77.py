'''
EXERCÍCIO 077: Contando Vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla = ('corrida','bike','nataçao','triathlon','peridizaçao','treinamento','muculaçao')

for palavra in tupla:
    a = palavra.count('a')
    e = palavra.count('e')
    i = palavra.count('i')
    o = palavra.count('o')
    u = palavra.count('u')
    print (f'palavra {palavra} tem {a+e+i+o+u} vogais')
