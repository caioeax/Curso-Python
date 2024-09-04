"""
Iterando strings com while
"""

#       012345678901
nome = 'Caio Eduardo'

i = 0
novoNome = ''

while i < len(nome):
    letra = nome[i]
    novoNome += f'*{letra}'
    i += 1

novoNome += "*"
print(novoNome)