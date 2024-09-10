from enum import Enum

class Estado(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de janeiro", "RJ")
    ACRE = ("Acre", "AC")
    ALAGOAS = ("Alagoas", "AL")
    AMAPA = ("Amapá", "AP")
    AMAZONAS = ("Amazonas", "AM")

    def __init__(self, nome, sigla) -> None:
        self.nome = nome
        self.sigla = sigla

    def get_nome(self):
        return self.nome

    def get_sigla(self):
        return self.sigla