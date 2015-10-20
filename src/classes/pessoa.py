class Pessoa:

    empresa = 'ACME'

    def __init__(self, nome, idade):
        # Não foi preciso declarar os atributos fora do construtor
        self.nome = nome
        self.idade = idade

    def primeiro_nome(self):
        return self.nome.split()[0]
