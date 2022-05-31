'''
EXERCÍCIO 043: Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = (float(input('Qual seu peso em kg?: ')))
altura = (float(input('Qual a sua altura em metros?: ')))
imc = (peso/(pow(altura,2)))

print ('seu imc é {:.2f}'.format(imc))

if imc < 18:
    print ('você está abaixo do peso')

elif imc > 18.5:
    print ('peso normal')

elif imc < 25:
    print ('peso normal')

elif imc > 25:
    print ('acima do peso')

elif imc < 30:
    print ('acima do peso')

elif imc > 30:
    print ('risco de obesidade')
