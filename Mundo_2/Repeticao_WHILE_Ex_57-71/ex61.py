'''
EXERCÍCIO 061: Progressão Aritmética v2.0
Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
'''


while True:
    try:
        primeiro_pa = (int(input('Digite o primeiro numero da PA: ')))
        razao_pa = (int(input('Digite a razao da PA: ')))
    except (ValueError,TypeError):
        continue
    else:
        break

c = 1
s=0
while c < 10:
    if c == 1:
        print(primeiro_pa, end=' ')
    print (primeiro_pa + razao_pa, end=' ')
    primeiro_pa+=razao_pa
    c+=1







