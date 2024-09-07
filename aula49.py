"""
Lista em python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - Indices e fatiamento
Metodos uteis: 
        append, insert, pop, del, clear, extend, +,
Create Read Update   Delete - > C R U D
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# del lista[2]
# print(lista)
# numero = lista[2]
# print(numero)
lista.pop()
ultimoValor = lista.pop()
print(lista, 'Removido,', ultimoValor)