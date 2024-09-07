"""
Tipo tupla - Uma lista imutável
"""
 
nomes = 'Maria', 'Helena', 'luiz' # Tipo de criacao de tupla
nomes = ('Maria', 'Helena', 'luiz') # Tipo de criacao de tupla
nomes = ['Maria', 'Helena', 'luiz']
nomes = tuple(nomes)
# nomes[1] = 'outro' -- Erro! Imutável.

print(nomes, type(nomes))