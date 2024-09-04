"""
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""

nome = 'Caio'
preco = 1000.95897643
# variavel = '%s, o preço é RS%.2f %s' % (nome, preco) # Erro pois tem mais parametros do que variáveis
variavel = '%s, o preço é RS%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é 0x%06x' % (15, 15))