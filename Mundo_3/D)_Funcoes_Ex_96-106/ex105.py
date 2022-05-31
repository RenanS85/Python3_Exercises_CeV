'''
Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
'''

from statistics import mean

def notas (*notas,sit=False): #OBS pode=se usar também **kwargs e já fazer o dicionário direto
    """
    :param n: notas dos alunos
    :param sit: mostrar situação da média dos alunos sit=True
    :return: dict() com total de notas, maior nota, menor nota, média e situação (if sit == True)
    """
    dic = {}
    l = []
    c=1
    for nota in notas:
        dic[f"nota {c}"] = nota
        l.append(nota)
        c+=1
    print (f'DICIONÀRIO {dic}')
    print (f'Maior nota {max(l)}')
    print(f'Menor nota {min(l)}')
    media = mean(l)
    print (f'Média = {media}')
    if sit:
        if media < 5:
            print ('Reprovado')
        elif 5 <= media <=7:
            print ('Boas Notas')
        elif 7 < media <=10:
            print ('Ótimas Notas')




notas (5.5,7,4,8,sit=True)
