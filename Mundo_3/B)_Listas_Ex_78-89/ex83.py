'''
EXERCÍCIO 083: Validando Expressões Matemáticas
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

exp = input('Digite uma expressão matemática: ')
join =' '.join(exp)
split = join.split()

if split.count('(') == split.count(')'):
    print ('VALIDADO')
else:
    print ('Invalido')




