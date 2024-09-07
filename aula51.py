"""
Lista em python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - Indices e fatiamento
Metodos uteis: 
        append -  Adiciona um item no final
        insert -  Adiciona um item no índice escolhido
        pop - Remove do final ou do índice escolhido
        del - apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
Create Read Update   Delete - > C R U D
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = lista_1 + lista_2  # --> Soma o conteudo da lista 1 com a lista 2 e faz a lista 3.
lista_1.extend(lista_2) # --> Pega o conteúdo da lista 2 e joga dentro da 1.
print(lista_1) 
print(lista_3)