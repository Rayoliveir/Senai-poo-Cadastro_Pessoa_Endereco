from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")

    def __init__(self, genero, caracter) -> None:
        self.genero = genero
        self.caracter = caracter

    def get_genero(self) -> str:
        return self.genero
    
    def get_caracter(self) -> str:
        return self.caracter