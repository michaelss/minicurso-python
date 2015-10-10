# Execute as linhas deste arquivo no modo interativo do Python3

# Pilhas
# --------------------------------

pilha = [1, 2, 3, 4]

pilha.append(5)

pilha.append(6)

pilha.pop()

pilha.append(7)

pilha.pop()


# Filas
# --------------------------------

from collections import deque

fila = deque([1, 2, 3, 4])

fila.append(5)

fila.append(6)

fila.popleft()

fila.append(7)

fila.popleft()


# Tuplas
# --------------------------------

# Tuplas parecem listas, mas são imutáveis e usualmente contêm elementos de tipos diferentes

t = 1000, 4321, 'olá!'

t[0]

t = (1000, 4321, 'olá!')

t[1] = 5432 # Não funciona pois tuplas são imutáveis


# Sets
# --------------------------------

# Set é uma coleção desordenada, sem elementos repetidos e com suporte a operações de conjuntos

centro = {'Palmas', 'Paraíso', 'Porto Nacional', 'Miracema', 'Lajeado', 'Palmas', 'Guaraí'}

'Lajeado' in centro

norte = {'Araguaína', 'Guaraí', 'Colinas', 'Araguatins'}

centro - norte

centro | norte

centro & norte


# Dicionários
# --------------------------------

# Dicionários são conhecidos como arrays associativos ou como mapas em outras linguagens

agenda = {'Maria': '9999-0000', 'José': '8888-1111', 'Ana': '9988-2222'}

agenda['Maria']

agenda['Joaquim'] = '8899-3333'

agenda.keys()

list(agenda.keys())

'Ana' in agenda

['{} = {}'.format(c, v) for c, v in agenda.items()]
