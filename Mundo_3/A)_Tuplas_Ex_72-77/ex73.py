'''
EXERCÍCIO 073: Tuplas com Times de Futebol
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
'''

times = ('América'
        ,'Athletico Paranaense'
        ,'Atlético - GO'
        ,'Atlético Mineiro'
        ,'Avaí'
        ,'Botafogo'
        ,'Ceará'
        ,'Corinthians'
        ,'Coritiba'
        ,'Cuiabá'
        ,'Chapecoense'
        ,'Fluminense'
        ,'Fortaleza'
        ,'Goiás'
        ,'Internacional'
        ,'Juventude'
        ,'Palmeiras'
        ,'Red Bull'
        ,'Santos '
        ,'São Paulo')

for c in range (0,5):
    print (f'O {c+1}º colocado é: {times[c]} ')
print('')
for c in range (19,15,-1):
    print(f'O {c+1}º colocado é: {times[c]} ')

ordem = sorted(times)
print (f'Em ordem afabética: {ordem}')

print (f'A chapecoense esta em {times.index("Chapecoense")+1}')





