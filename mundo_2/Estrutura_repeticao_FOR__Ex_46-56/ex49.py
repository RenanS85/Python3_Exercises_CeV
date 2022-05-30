'''
EXERCÍCIO 049: Tabuada v2.0
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
'''

num = float(input('Digite um numero: '))
print ('veremos a tabuada desse numero"')
print('')
c=1
for n in range (1,11):
    print(f'{num:>2} X {c:>2.2f} = {n*c:>3.2f}')
    c+=1


