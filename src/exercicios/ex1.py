# A.
# Crie uma função que receba um inteiro com a quantidade de alunos e retorne
# uma string na forma "O número de alunos é <qtd>". Se a quantidade de alunos
# for maior que 10, no lugar de <qtd>, deve aparecer "muitos", senão, é mostrada
# a quantidade informada mesmo.
def alunos(qtd):
    # TODO
    return


# B.
# Retorne as duas primeiras e as duas últimas letras da string passada como
# parâmetro. Se a string tiver menos de duas letras, retorne uma string vazia.
def dois_lados(s):
    # TODO
    return


# C.
# Dadas duas strings a e b, retorne as duas separadas por um espaço. Mas troque
# os dois primeiros caracteres de cada string.
# Exemplo:
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assuma que a e b tenham 2 ou mais caracteres.
def mistura(a, b):
    # TODO
    return



def test(recebido, esperado):
    if recebido == esperado:
        prefixo = ' OK '
    else:
        prefixo = '  X '
    print('%s recebido: %s esperado: %s' % (prefixo, repr(recebido), repr(esperado)))


def main():
    print('alunos')
    test(alunos(4), 'O número de alunos é 4')
    test(alunos(9), 'O número de alunos é 9')
    test(alunos(10), 'O número de alunos é muitos')
    test(alunos(99), 'O número de alunos é muitos')

    print()
    print('dois_lados')
    test(dois_lados('spring'), 'spng')
    test(dois_lados('Hello'), 'Helo')
    test(dois_lados('a'), '')
    test(dois_lados('xyz'), 'xyyz')

    print()
    print('mistura')
    test(mistura('mix', 'pod'), 'pox mid')
    test(mistura('dog', 'dinner'), 'dig donner')
    test(mistura('gnash', 'sport'), 'spash gnort')
    test(mistura('pezzy', 'firm'), 'fizzy perm')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
