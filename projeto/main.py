import os
os.system("cls || clear")

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.estado import Estado


pessoa_1 = Pessoa(1525, "Joana", "25/08/1998", "7199999-9999", "joana@gmail.com", Sexo.FEMININO, 
                  Endereco("Rua dinamarca", "250", "Centro", "48900-600", "Xique-xique", Estado.BAHIA))

print(pessoa_1)