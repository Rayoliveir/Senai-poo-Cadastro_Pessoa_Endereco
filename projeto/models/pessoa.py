from models.endereco import Endereco
from models.enums.sexo import Sexo


class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: str, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            "*== DADOS DA PESSOA ==*"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.dataNascimento}"
            f"\nData de Nascimento: {self.dataNascimento}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nSexo: {self.sexo.get_caracter()} - {self.sexo.get_genero()}"
            f"\n\n-- ENDEREÇO -- {self.endereco}\n"
            )
    