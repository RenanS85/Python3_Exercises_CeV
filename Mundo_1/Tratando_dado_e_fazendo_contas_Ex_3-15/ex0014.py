'''
EXERCÍCIO 014: Conversor de Temperaturas
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
'''

print('bora conververter graus celsius pra fahrenheit')
#(0 °C × 9/5) + 32 = 32 °F
tempcels = float(input('Escolha a temperatura em celsius: '))
f = ((tempcels*(9/5))+32)
print (f'A tempoeratura em fahrenheit é {f}ºF')