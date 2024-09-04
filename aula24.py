# Operadores in e not in
# String são iteráveis
# 0 1 2 3
# C a i o
# -4-3-2-1

# nome = 'Caio'

# print(nome[2])

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')