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

print(variavel)

print(variavel2)

print('Olá ', variavel)

print('Olá', variavel + '.')

print("Olá ' ")

print('Olá \' ')

print(r'Olá \' ')

variavel[0] # Acesso a uma posição da string

variavel[0] = 'm' # Strings são IMUTÁVEIS


# Listas
# --------------------------------

numeros = [1, 3, 9, 16, 25, 36]

numeros

numeros[1]

numeros[1] = 4 # Listas são MUTÁVEIS (ao contrário de strings)

numeros[6] = 49

numeros.append(49)

numeros + [64, 81, 100]

numeros = numeros + [64, 81, 100]
