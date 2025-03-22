import random

class Contato:
    def __init__(self, telefone: int, cpf: str):
        self.id_contato = random.randint(0, 1000)
        self.telefone = telefone
        self.cpf = cpf

class Pessoa:
    def __init__(self, cpf: str, nome: str):
        self.cpf = cpf
        self.nome = nome
