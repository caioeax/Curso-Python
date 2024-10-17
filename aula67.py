"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor padrão será
usado.
Refatorar: editar seu código
"""

def soma(x, y, z=None):
    print(x + y)
    print(x + y + z)
    print(y + z)
    print()

soma(1, 2, 7)
soma(3, 5, 32)
soma(100, 200, 700)