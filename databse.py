from structs import Contato, Pessoa
from typing import List

class Databse:
    def __init__(self):
        self.pessoas: List[Pessoa] = []
        self.contatos: List[Contato] = []

    def add_pessoa(self, cpf: str, nome: str):
        pessoa = Pessoa(cpf, nome)
        self.pessoas.append(pessoa)

    def add_contato(self, telefone: int, cpf: str) -> None|bool:
        if not self.get_pessoa(cpf):
            return False
        contato = Contato(telefone, cpf)
        self.contatos.append(contato)

    def get_pessoa(self, cpf: str) -> Pessoa|None:
        for pessoa in self.pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None
    
    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
            return

        for contato in self.contatos:
            pessoa = self.get_pessoa(contato.cpf)
            if pessoa:
                print(f"Nome: {pessoa.nome} | Telefone: {contato.telefone}")
            else:
                print(f"CPF não encontrado para o contato {contato.telefone}")