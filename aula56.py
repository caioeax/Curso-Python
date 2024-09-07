"""
enumerate - enumera iteráveis (indices)
"""

lista = ['Maria', 'Helena', 'luiz']
lista.append('Joao')

listaEnumerada = enumerate(lista)

# for item in listaEnumerada: # "gasta" as palavras e nao da pra printar novamente.
#     print(item)

# print(listaEnumerada) # printando em enumerate()

#for item in enumerate(lista): # tupla enumerada que foi desempacotada e mostrada um por um
#    indice, nome = item
#    print(indice, nome)

for indice, nome in enumerate(lista): # pode printar novamente e reutilizar
    print(indice, nome, lista[indice])

# print(list(listaEnumerada)) # Prova real que gastou
# print(list(enumerate(lista))) # Prova real que pode reutilizar.

for tuplaEnumerada in enumerate(lista):
    print('FOR da tupla')
    for valor in tuplaEnumerada:
        print(f'{valor}')
