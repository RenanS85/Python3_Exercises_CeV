'''
Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.

Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
'''
from time import sleep
from pacote_utilidades.interface import *
from pacote_utilidades.cadastros import *

arq = 'ex115.txt'

while True:
    resposta = menu(['Listar pessoas cadastradas','Cadastrar Pessoa', 'Sair do Sistama'])
    if resposta==1:
        lerArquivo(arq)
    elif resposta==2:
        #cadastrar uma nova pessoa
        print ('CADASTRO DE NOVA PESSOA')
        nome = str(input('Nome: ')).strip().title()
        idade = input('Idade: ')
        cadastro(arq, nome, idade)
    elif resposta==3:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print ('ERRO - DIGITE UMA OPÇÂO VÀLIDA')
    sleep(2)
