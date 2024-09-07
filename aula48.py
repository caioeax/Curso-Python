"""
Lista em python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - Indices e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +
"""

string = 'abcde' # 5 caracteres (len)
# lista = list()
# print(lista, type(lista))
# print(bool([])) # falsy

#          0    1           2         3    4
lista =  [123, True, 'Caio Eduardo', 1.2, []]
print(lista)
print(lista[2])

lista[2] = 'Gugay'
lista[3] = 2.5

print(lista)