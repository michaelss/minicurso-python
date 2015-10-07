# Execute as linhas deste arquivo no modo interativo do Python3

# If
# --------------------------------

nome = 'Joana Fonseca'

if len(nome) > 10:
    print('Nome grande')
elif len(nome) < 5:
    print('Nome curto')
else:
    print('Nome médio')


tipo = 'curto' if len(nome) < 5 else 'longo'


# For
# --------------------------------

lista = ['Joana', 'Ana', 'Mariana', 'Fabiana']

for x in lista:
    print(x)

for i, x in enumerate(lista):
    print(i, x)

for x in sorted(lista):
    print(x)


# Range
# --------------------------------

range(5)

for x in range(5):
    print(x)

for i in range(len(lista)):
    print(i, lista[i])

for x in range(2,5):
    print(x)


# List Comprehensions
# --------------------------------

quadrados = []
for x in range(10):
    quadrados.append(x**2)


quadrados = [x**2 for x in range(10)]

quadrados = [x**2 for x in range(10) if x % 2 == 0]
