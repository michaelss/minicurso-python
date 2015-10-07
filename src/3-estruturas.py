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
