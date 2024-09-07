"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# lista_a = ['caio', 'eduardo']
# lista_b = lista_a

# lista_a[0] = 'Qualquer coisa'
# print(lista_b)

lista_c = ['caio', 'eduardo']
lista_d = lista_c.copy()

lista_c[0] = 'Qualquer coisa'
print(lista_d)