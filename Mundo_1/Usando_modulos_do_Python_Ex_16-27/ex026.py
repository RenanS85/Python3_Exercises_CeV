'''
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
'''

frase = input(('digite uma frase: ')).upper()
xA = frase.count('a')
pri_pos = frase.find('a')
ult_pos = frase.rfind('a')
print ('a letra "A" aparede {} vezes'.format(pri_pos))
print ('a primera posição do "A" é:', pri_pos)
print ('a ultima posição de "A" é:', ult_pos)

