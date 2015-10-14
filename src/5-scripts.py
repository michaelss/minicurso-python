import sys

def main():
    # Receber argumentos
    if len(sys.argv) > 1:
       print(sys.argv)

    # Entrada do usuário
    s = input('Digite seu nome: ')
    print(s)


# Quando temos um script, é comum reunir o código em funções. Neste caso, faz-se
# necessário definir a primeira função a ser chamada.
if __name__ == '__main__':
   main()
