'''Cliente das classes criadas. Execute com "python classes/cliente_classes.py"'''

from pessoa import Pessoa

jose = Pessoa('José da Silva', 25)

print('Primeiro nome de José: ' + jose.primeiro_nome())

print('Empresa: ' + jose.empresa)

print('Empresa: ' + Pessoa.empresa)





# ----------------------------------
# Atributos de objetos x atributos de classes

jose.empresa = 'CEULP'

print('Empresa: ' + jose.empresa)

Pessoa.empresa = 'ULBRA'

print('Empresa: ' + Pessoa.empresa)

print('Empresa de novo objeto: ' + Pessoa('Pedro Paulo', 12).empresa)



# ----------------------------------
# Outra forma de criar e usar objetos

# ana = Pessoa('Ana Santos', 23)
#
# print('Primeiro nome de Ana: ' + Pessoa.primeiro_nome(ana))



# ----------------------------------
# Herança

# import funcionario as func
#
# maria = func.Funcionario('Maria de Souza', 26)
#
# print('Úlimo nome: ' + maria.ultimo_nome())



# ----------------------------------
# Duck typing

# def duck(obj):
#     print(obj.primeiro_nome())
#
# duck(ana)
#
# from empresa import Empresa
#
# empresa = Empresa()
#
# duck(empresa)
