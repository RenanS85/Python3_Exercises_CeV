'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto (nascimento):
    import datetime
    hoje = datetime.date.today().year
    idade = hoje-nascimento
    if idade < 16:
        print (f'com {idade}anos p voto é negado')
    elif 16 < idade < 18 or idade >70:
        print (f'com {idade} anos o voto é opcional')
    elif 18 <= idade:
        print (f'com idade {idade} anos o voto é obrigatorio')

n=int(input('em que ano vc nasceu: '))
voto(n)

