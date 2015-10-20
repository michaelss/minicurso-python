
# Para testar, basta executar o arquivo. Ele possui uma bateria de testes ao
# final.


# A.
# Dada uma lista de palavras retorne a quantidade de palavras cujo tamanho seja
# maior que 2 e que o primeiro caractere seja igual ao último.
def extremos_iguais(palavras):
    # TODO
    return


# B.
# Dada uma lista de palavras, retorne-as em ordem alfabética, sendo que as
# palavras iniciadas com 'x' devem vir antes das demais.
def inicia_x(palavras):
    # TODO
    return



def test(recebido, esperado):
    if recebido == esperado:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s recebido: %s esperado: %s' % (prefix, repr(recebido), repr(esperado)))


# Calls the above functions with interesting inputs.
def main():
    print('extremos_iguais')
    test(extremos_iguais(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(extremos_iguais(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(extremos_iguais(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('inicia_x')
    test(inicia_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(inicia_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(inicia_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


if __name__ == '__main__':
    main()
