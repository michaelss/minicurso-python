# Execute as linhas deste arquivo no modo interativo do Python3

# Operações
# --------------------------------

1 + 2

(2 + 2) * 3

17 / 3

17 // 3 # Resultado arredondado da divisão

17 % 3 # Resto da divisão


# Strings, variáveis e atribuições
# --------------------------------

variavel = "Mundo"

variavel

print(variavel)

print(variavel2)

print('Olá ', variavel)

print('Olá', variavel + '.')

print('Olá \' ')

print(r'Olá \' ')

print('Olá {}'.format(variavel))

variavel[0] # Acesso a uma posição da string

variavel[0] = 'm' # Erro: Strings são IMUTÁVEIS

inteiro = 20

variavel + inteiro # Erro: não se pode somar string e inteiro

variavel + str(inteiro) # Concatenando string e inteiro

variavel = "10"

int(variavel) + inteiro # Somando

a, b = 1, 2


# Listas
# --------------------------------

vazia = []

vazia

numeros = [1, 3, 9, 16, 25, 36]

numeros

numeros[1]

numeros[1] = 4 # Listas são MUTÁVEIS (ao contrário de strings)

numeros[6] = 49 # Erro: não se pode definir item em posição inexistente

numeros.append(49) # Adição de novo item

numeros + [64, 81, 100]

numeros = numeros + [64, 81, 100]

aninhada = [[1, 2, 3], ['a', 'b', 'c']]

aninhada[1][0]


# Slices
# --------------------------------

numeros[0:3]

numeros[1:-1]

numeros[2:]

numeros[:-2]
