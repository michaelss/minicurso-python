
from pessoa import Pessoa

class Funcionario(Pessoa):

    print('''Mostrando que uma classe pode ter instruções arbitrárias, além de métodos e atributos.''')

    def ultimo_nome(self):
        return self.nome.split()[-1]
