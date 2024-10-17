"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome ocm sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma (x, y, z):
    print(f'{x=} {y=} {z=}', "| x + y + z =", x + y + z) # Definição

# print(soma) # Printando o local da memória
# print(soma(1, 2)) # Redundante

soma(1, 2, 3) # Tipo 1 não nomeado
soma(y=2, z=3, x=1) # Tipo 1 nomeado

soma(2, 1, 3) # Tipo 2 não nomeado
soma(y=1, z=3, x=2) # Tipo 2 nomeado