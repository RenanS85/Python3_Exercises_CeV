'''EXERCÍCIO 022: Analisador de Textos
Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços)
> Quantas letras tem o primeiro nome.
'''

nome = input ('Digite seu nome: ')
nomeupper = nome.upper()
nomelower = nome.lower()
espaços = nome.count(' ')
caracteres = len(nome)
nome_separado = nome.split()
primeironome = nome_separado[0]



print ('esse é o nome em uppercase', nomeupper)
print ('ese é o nome em lowercase', nomelower)
print ('essa é a quantidade de letras, tirando os espaços:', caracteres-espaços)
print('essa é a quantidade de letras do primeiro nome', len(primeironome))


