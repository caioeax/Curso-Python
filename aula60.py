"""
Lista de listas e seus indices
"""

salas = [['Isabela', 'Caio', ], ['Elaine', ], ['Luiz', 'João', 'Eduarda', ]]


# print(salas[0]) # ['Isabela', 'Caio', ]
# print(salas[1][0]) # Elaine
# print(salas[2][3][2]) # 20

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)