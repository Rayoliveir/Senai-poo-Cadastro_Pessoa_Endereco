from models.enums.estado import Estado


class Endereco:
    def __init__(self, longradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: Estado) -> None:
        self.longradouro = longradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (
            f"\nLongradouro: {self.longradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nEstado: {self.uf.get_nome()}"
            f"\nUF: {self.uf.get_sigla()}"
        )