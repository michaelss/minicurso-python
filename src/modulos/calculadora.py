'''Módulo com operações matemáticas.'''

def somar(op1, op2):
    '''Função para somar dois números.'''
    return op1 + op2

def subtrair(op1, op2):
    '''Função para subtrair o segundo número do primeiro.'''
    return op1 - op2

def dividir(op1, op2):
    '''Função dividir o primeiro pelo segundo operador.'''
    try:
        return op1 / op2
    except ZeroDivisionError:
        print('Não se pode dividir por 0.')
