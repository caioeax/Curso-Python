"""
Introdução ao desempacotamento
"""

# nomes = ['Caio','Rapha','Isabela']
# nome1, nome2, nome3 = nomes
# nome1, nome2 = nomes # erro

*_,  nome2 = ['Caio','Rapha','Isabela']

print(_, nome2)

# _,  nome2, *resto = ['Caio','Rapha','Isabela']

# print(_, nome2, resto)