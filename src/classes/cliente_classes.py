'''Cliente das classes criadas. Execute com "python classes/cliente_classes.py"'''

import pessoa

p = pessoa.Pessoa('José da Silva', 25)

print(p.primeiro_nome())

print(p.empresa)

print(pessoa.Pessoa.empresa)














# ----------------------------------
# O que será impresso nas linhas abaixo?

# p.empresa = 'CEULP'
#
# pessoa.Pessoa.empresa = 'ULBRA'
#
# print(pessoa.Pessoa.empresa)
#
# print(p.empresa)
