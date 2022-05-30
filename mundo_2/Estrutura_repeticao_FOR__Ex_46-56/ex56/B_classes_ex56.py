from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


class Homem(Pessoa):
    pass


class Mulher(Pessoa):
    pass