'''
EXERCÍCIO 085: Listas com Pares e Ímpares
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

numeros = list()
par = list()
impar = list()
lista = list()
for n in range (1,8):
    numeros.append(int(input(f'Digite o {n}º numero: ')))
for num in numeros:
    if num%2==0:
        par.append(num)
        par.sort()
    if num%2==1:
        impar.append(num)
        impar.sort()
lista.append(par)
lista.append(impar)
print(lista)

