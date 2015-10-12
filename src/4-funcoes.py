

# Definição de funções
# --------------------------------

def somar(op1, op2):
    return op1 + op2

somar(1, 2)

somar(op2 = 3, op1 = 2)


# Argumentos padrão
# --------------------------------

def subtrair(op1, op2 = 0):
    return op1 + op2

subtrair(1)

subtrair(10, 2)


# Keyword arguments
# --------------------------------

# Recebendo uma lista:

def somar(op1, *args):
    soma = op1
    for num in args:
        soma += num
    return soma

somar(1, 2, 3, 4, 5)


# Recebendo um dicionário:

def fun(op1, **kwargs):
    return kwargs

fun('ok', chave1='valor1', chave2='valor2')


# Recebendo uma lista e um dicionário

def mix(*args, **kwargs):
    print(args)
    print(kwargs)

fun(1, 2, 3, 4, 5, chave1='valor1', chave2='valor2')
